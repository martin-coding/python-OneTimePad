"""Dialog window to prompt the user generating settings and info."""

from typing import TYPE_CHECKING

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QDialog

from one_time_pad.dialog import Dialog
from one_time_pad.generated.ui_generate_dialog import Ui_GenerateDialog
from one_time_pad.otp import write_random_keyfile
from one_time_pad.worker import Worker

if TYPE_CHECKING:
    from one_time_pad.main_window import MainWindow


class GenerateDialog(QDialog, Ui_GenerateDialog):
    """Dialog window to prompt the user generating settings and info."""

    def __init__(self, parent: "MainWindow") -> None:
        """Show a generate window with settings."""
        super().__init__()
        self.setupUi(self)
        self.directory = parent.send_key_dir
        self.main_window = parent

        self.generateButton.clicked.connect(self._start_generating)
        self.doneGeneratingButton.clicked.connect(lambda: self.done(QDialog.DialogCode.Accepted))

        self.threadpool = QThreadPool()
        self.exec()

    def _progress_report(self, percentage: int) -> None:
        self.generateProgressBar.setValue(percentage)

    def _error_received(self, e: Exception) -> None:
        if isinstance(e, OSError):
            Dialog("error", e.strerror, e.filename)

    def _thread_complete(self) -> None:
        self.generateButton.setEnabled(True)
        self.main_window.en_dir_model.layoutChanged.emit()

    def _start_generating(self) -> None:
        file_name = self.keyNameEdit.text() if self.keyNameEdit.text() else self.keyNameEdit.placeholderText()
        size_base: str = self.fileSizeEdit.text() if self.fileSizeEdit.text() else self.fileSizeEdit.placeholderText()
        size_multiplier = 1024 ** self.unitSelect.currentIndex()
        keyfile_path = self.directory / (file_name + ".key")
        if keyfile_path.exists():
            Dialog("warn", "Keyfile exists", "This keyfile already exists. Delete it first.")
            return
        if not size_base.isdigit():
            Dialog("error", "Size not Integer", "Size must be of type integer.")
            return

        total_size_b = int(size_base) * size_multiplier
        self.generateProgressBar.setValue(0)

        worker = Worker(write_random_keyfile, keyfile_path, total_size_b)
        worker.signals.finished.connect(self._thread_complete)
        worker.signals.progress.connect(self._progress_report)
        worker.signals.error.connect(self._error_received)

        self.generateButton.setEnabled(False)
        self.threadpool.start(worker)
