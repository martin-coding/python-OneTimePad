"""one-time-pad package."""

import sys

from PySide6.QtWidgets import QApplication

from one_time_pad.main_window import MainWindow


def main() -> None:
    """Jump in point."""
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
