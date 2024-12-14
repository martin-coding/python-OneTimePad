"""Dialog window for displaying data to user."""

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from one_time_pad.generated.ui_dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """Dialog window for displaying data to user."""

    def __init__(self, dialog_type: str, title: str, description: str) -> None:
        """Show a dialog window with specified messages."""
        super().__init__()
        self.setupUi(self)

        dialog_settings = {
            "info": {
                "icon": QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation),
                "title": "Information",
            },
            "warn": {
                "icon": QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning),
                "title": "Warning",
            },
            "error": {
                "icon": QIcon.fromTheme(QIcon.ThemeIcon.DialogError),
                "title": "Error",
            },
        }

        settings = dialog_settings.get(
            dialog_type,
            {
                "icon": QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation),
                "title": "Default",
            },
        )

        self.setWindowIcon(settings["icon"])
        self.setWindowTitle(settings["title"])
        self.messageTitle.setText(title)
        self.messageDescription.setText(description)
        self.exec()
