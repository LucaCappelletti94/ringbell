import sys
from environments_utils import is_notebook
from .ringbell import RingBell


def auto_ringbell(
    minimum_execution_time: int = 60,
    only_exceptions: bool = False
):
    """Plays good or bad sound when the execution takes more than `minimum_execution_time` seconds.
    
    Parameters
    ---------------------
    minimum_execution_time: int = 60
        Minimum time to wait for before playing
        the ringbell.
    only_exceptions: bool = False
        Whether to play sound only for exceptions.
    """

    def play_bad_sound():
        """Plays the bad sound when exceptions happen."""
        RingBell(
            sample="wrong_answer",
            minimum_execution_time=minimum_execution_time,
        ).play()

    def play_good_sound():
        """Plays the good sound when execution completes successfully."""
        RingBell(
            sample="positive_notification",
            minimum_execution_time=minimum_execution_time,
            verbose= not only_exceptions
        ).play()

    if is_notebook():
        from IPython import get_ipython
        from IPython.core.interactiveshell import ExecutionResult

        def jupyter_notebook_wrapper(
            execution_result: ExecutionResult
        ):
            if execution_result.error_in_exec:
                play_bad_sound()
            else:
                play_good_sound()

        ip = get_ipython()
        ip.events.register("pre_run_cell", RingBell.reset_start_time)
        ip.events.register("post_run_cell", jupyter_notebook_wrapper)
    else:
        backup = sys.excepthook

        def script_exception_wrapper(exctype, value, traceback):
            play_bad_sound()
            backup(exctype, value, traceback)

        sys.excepthook = script_exception_wrapper