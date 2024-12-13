"""Main window of application."""
from pathlib import Path

from platformdirs import user_data_dir
from PySide6.QtCore import QItemSelection
from PySide6.QtWidgets import QHeaderView, QMainWindow, QTreeView

from one_time_pad import otp
from one_time_pad.dialog import Dialog
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
        send_key_dir = keystore_directory / "send"
        receive_key_dir = keystore_directory / "receive"

        send_key_dir.mkdir(parents=True, exist_ok=True)
        receive_key_dir.mkdir(parents=True, exist_ok=True)

        # Set up views
        self.en_dir_model = self._setup_view(
            send_key_dir, self.encryptKeyfilesView, self.encrypt_view_changed,
        )
        self.de_dir_model = self._setup_view(
            receive_key_dir, self.decryptKeyfilesView, self.decrypt_view_changed,
        )

        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)

    def encrypt(self) -> None:
        """Encrypt."""
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
            Dialog("error", "Key too short", "The selected key has not enough free bytes remaining. Try selecting a diffrent one")
            return
        self.outputCiphertextField.setPlainText(ciphertext)
        self.en_dir_model.layoutChanged.emit()

    def decrypt(self) -> None:
        """Decrypt."""
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
            Dialog("error", "Key too short", "The selected key has not enough free bytes remaining. Try selecting a diffrent one")
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

    def encrypt_view_changed(self, selected: QItemSelection, deselected: QItemSelection) -> None:  # noqa: ARG002 ignore deselected
        """Call when encrypt view selection changes."""
        self.view_changed(selected, self.en_dir_model, "encrypt_keyfile")

    def decrypt_view_changed(self, selected: QItemSelection, deselected: QItemSelection) -> None: # noqa: ARG002 ignore deselected
        """Call when decrypt view selection changes."""
        self.view_changed(selected, self.de_dir_model, "decrypt_keyfile")

    def view_changed(self, selected: QItemSelection, dir_model: KeyfileDirModel, attribute_name: str) -> None:
        """Set selected keyfile attribute."""
        indexes = selected.indexes()
        if indexes:
            file_path = dir_model.filePath(indexes[0])
            setattr(self, attribute_name, Path(file_path))
