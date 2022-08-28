import sys
from environments_utils import is_notebook
from .ringbell import RingBell


def auto_ringbell(
    minimum_execution_time: int = 60,
    only_exceptions: bool = False,
    good_sound: str = "positive_notification",
    bad_sound: str = "wrong_answer",
):
    """Plays good or bad sound when the execution takes more than `minimum_execution_time` seconds.
    
    Parameters
    ---------------------
    minimum_execution_time: int = 60
        Minimum time to wait for before playing
        the ringbell.
    only_exceptions: bool = False
        Whether to play sound only for exceptions.
    good_sound: str = "positive_notification"
        The sound to play when execution is nominal.
    bad_sound: str = "wrong_answer"
        The sound to play when execution goes wrong.
    """

    def play_bad_sound():
        """Plays the bad sound when exceptions happen."""
        RingBell(
            sample=bad_sound,
            minimum_execution_time=minimum_execution_time,
        ).play()

    def play_good_sound():
        """Plays the good sound when execution completes successfully."""
        RingBell(
            sample=good_sound,
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