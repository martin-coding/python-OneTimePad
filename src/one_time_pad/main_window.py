"""Main window of application."""

import shutil
from pathlib import Path
from threading import Thread

from platformdirs import user_data_dir
from PySide6.QtCore import QItemSelection
from PySide6.QtWidgets import QFileDialog, QHeaderView, QMainWindow, QTreeView

from one_time_pad import otp
from one_time_pad.dialog import Dialog
from one_time_pad.generate_dialog import GenerateDialog
from one_time_pad.generated.ui_main_window import Ui_MainWindow
from one_time_pad.keyfile_dir_model import KeyfileDirModel


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window of application."""

    def __init__(self) -> None:
        """Init main window."""
        super().__init__()
        self.setupUi(self)

        self.encrypt_keyfile: Path = None
        self.decrypt_keyfile: Path = None

        keystore_directory = Path(user_data_dir("one-time-pad", "martin-coding")) / "keystore"
        self.send_key_dir = keystore_directory / "send"
        self.receive_key_dir = keystore_directory / "receive"

        self.send_key_dir.mkdir(parents=True, exist_ok=True)
        self.receive_key_dir.mkdir(parents=True, exist_ok=True)

        self.en_dir_model = self._setup_view(
            self.send_key_dir,
            self.encryptKeyfilesView,
            self.encrypt_view_changed,
        )
        self.de_dir_model = self._setup_view(
            self.receive_key_dir,
            self.decryptKeyfilesView,
            self.decrypt_view_changed,
        )

        self.encryptButton.clicked.connect(self._encrypt)
        self.decryptButton.clicked.connect(self._decrypt)
        self.enGenerateButton.clicked.connect(self._generate_keyfile)
        self.enExportButton.clicked.connect(self._export_keyfile)
        self.enImportButton.clicked.connect(lambda: self._import_keyfile(self.send_key_dir))
        self.enDeleteButton.clicked.connect(lambda: self._delete_keyfile(self.encrypt_keyfile))
        self.deDeleteButton.clicked.connect(lambda: self._delete_keyfile(self.decrypt_keyfile))
        self.deAddButton.clicked.connect(lambda: self._import_keyfile(self.receive_key_dir))

    def _export_keyfile(self) -> None:
        if not self.encrypt_keyfile:
            Dialog("info", "No keyfile", "No keyfile selected. Try selecting a key to your left.")
            return
        export_file, _ = QFileDialog.getSaveFileName(self, "Export to:", "", "Keyfile (*.key)")
        if export_file:
            copy = Thread(target=shutil.copy, name="Export key", args=(self.encrypt_keyfile, export_file))
            copy.start()

    def _import_keyfile(self, location: Path) -> None:
        import_file, _ = QFileDialog.getOpenFileName(self, "Import file:", "", "Keyfile (*.key)")
        if import_file:
            copy = Thread(target=shutil.copy, name="Import key", args=(import_file, location))
            copy.start()

    def _delete_keyfile(self, keyfile: Path) -> None:
        if keyfile and keyfile.exists():
            metafile = keyfile.parent / (keyfile.stem + ".meta")
            keyfile.unlink()
            metafile.unlink()

    def _generate_keyfile(self) -> None:
        GenerateDialog(self)

    def _encrypt(self) -> None:
        message = self.inputMessageField.toPlainText()
        if self.encrypt_keyfile is None:
            Dialog("info", "No keyfile", "No keyfile selected. Try selecting a key to your left.")
            return
        if message == "":
            Dialog("info", "Message empty", "Message input field empty. Nothing to encrypt.")
            return
        try:
            ciphertext = otp.encode_data(self.encrypt_keyfile, message)
        except OverflowError:
            Dialog("error", "Overflow Error", "The remaining keyfile data is out of range.")
            return
        if ciphertext is None:
            Dialog("error", "Key too short", "The selected key has not enough free bytes remaining. Try selecting a different one")
            return
        self.outputCiphertextField.setPlainText(ciphertext)
        self.en_dir_model.layoutChanged.emit()

    def _decrypt(self) -> None:
        ciphertext = self.inputCiphertextField.toPlainText()
        if self.decrypt_keyfile is None:
            Dialog("info", "No keyfile", "No keyfile selected. Try selecting a key to your left.")
            return
        if ciphertext == "":
            Dialog("info", "Message empty", "Message input field empty. Nothing to decrypt.")
            return
        try:
            message = otp.decode_data(self.decrypt_keyfile, ciphertext)
        except ValueError as e:
            Dialog("error", e.args[0], "Input is most likely no correct.")
            return
        except UnicodeError as e:
            Dialog("error", e.args[0], "Your selected key is probably not the one used for encryption.")
            return
        if message is None:
            Dialog("error", "Key too short", "The selected key has not enough free bytes remaining. Try selecting a different one")
            return
        self.outputMessageField.setPlainText(message)
        self.de_dir_model.layoutChanged.emit()

    def _setup_view(self, directory: Path, view: QTreeView, callback: callable) -> KeyfileDirModel:
        dir_model = KeyfileDirModel(directory.as_posix())
        view.setModel(dir_model)
        view.setRootIndex(dir_model.index(directory.as_posix()))
        view.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        selection_model = view.selectionModel()
        selection_model.selectionChanged.connect(callback)
        return dir_model

    def encrypt_view_changed(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        """Call when encrypt view selection changes."""
        if deselected.indexes():
            self.encrypt_keyfile = None
        self.view_changed(selected, self.en_dir_model, "encrypt_keyfile")

    def decrypt_view_changed(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        """Call when decrypt view selection changes."""
        if deselected.indexes():
            self.decrypt_keyfile = None
        self.view_changed(selected, self.de_dir_model, "decrypt_keyfile")

    def view_changed(self, selected: QItemSelection, dir_model: KeyfileDirModel, attribute_name: str) -> None:
        """Set selected keyfile attribute."""
        indexes = selected.indexes()
        if indexes:
            file_path = dir_model.filePath(indexes[0])
            setattr(self, attribute_name, Path(file_path))
