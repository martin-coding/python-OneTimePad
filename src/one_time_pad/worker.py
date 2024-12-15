"""Worker module."""

import logging
from collections.abc import Callable
from typing import ParamSpec, TypeVar

from PySide6.QtCore import QObject, QRunnable, Signal, Slot

P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger(__name__)


class WorkerSignals(QObject):
    """Defines the signals available from a running worker thread.

    Supported signals are:
    - finished
    - error
    - result
    - progress

    """

    finished = Signal()
    error = Signal(Exception)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """Worker thread.

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    """

    def __init__(self, fn: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> None:
        """Create a worker."""
        super().__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self) -> None:
        """Initialise the runner function with passed args, kwargs."""
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            logger.exception("Error in worker thread")
            self.signals.error.emit(e)
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
