"""Custom implementation of the QFileSystemModel."""
from pathlib import Path

from PySide6.QtCore import QDir, QModelIndex, QObject, Qt
from PySide6.QtWidgets import QFileSystemModel

from one_time_pad.otp import read_pos_metadata


class KeyfileDirModel(QFileSystemModel):
    """Custom data model for keyfile storage."""

    def __init__(self, directory: str, parent: QObject = None) -> None:
        """Init KeyfileDirModel."""
        super().__init__(parent)
        self.setNameFilters(["*.key"])
        self.setNameFilterDisables(False)
        self.setFilter(QDir.Files | QDir.NoDotAndDotDot)
        self.setRootPath(directory)
        self.headers = ["Name", "Size", "Remaining"]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> str:
        """Return the data for the given role and section in the header with the specified orientation."""
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None

    def columnCount(self, index: QModelIndex) -> int:
        """Return the number of columns for the children of the given parent."""
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> str:
        """Return the data stored under the given role for the item referred to by the index."""
        if role == Qt.DisplayRole and self.headers[index.column()] == "Remaining":
            file_info = self.fileInfo(index)
            if file_info.isFile():
                path = Path(file_info.absoluteFilePath())
                used_data = read_pos_metadata(path)
                total_data = file_info.size()
                return self.human_readable_size(total_data - used_data)
            return ""
        return super().data(index, role)

    def human_readable_size(self, size: float, decimal_places: int =2 ) -> str:
        """Return the file size with appropriate units."""
        for unit in ["B", "KiB", "MiB", "GiB", "TiB"]:
            if size < 2**10:
                return f"{size:.{decimal_places}f} {unit}"
            size /= 1024.0
        return None
