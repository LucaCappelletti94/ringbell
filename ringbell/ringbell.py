from typing import List
import os
import random
from time import time
from environments_utils import is_notebook
from .utils import InvisibleAudio
from userinput.utils import must_be_in_set
import simpleaudio

__all__ = ["RingBell"]


class RingBell:

    START_TIME = time()

    def __init__(
        self,
        sample: str = "microwave",
        minimum_execution_time: int = 0,
        verbose: bool = True
    ):
        """Create a new RingBell.

        Parameters
        ------------------------------------------
        sample: str = "microwave"
            Name of one of the available samples.
            Use the `RingBell.available_samples()` method
            to get a comprehensive list of the available sounds.
            Use 'random' for choosing a random sample.
            If the provided element is not in the set, we will check for
            a possible path.
        minimum_execution_time: int = 0
            The minimum execution time to wait for to play the sound.
            Within normal Python scripts, this time is counted from when
            this package is loaded.
            Within Jupyter Notebooks, this time is counted from when the
            last cell started.
        verbose: bool = True
            Whether to play the audio.

        Raises
        ----------------------
        ValueError
            If the given sample does not exist.
        ValueError
            If the given path does not correspond to a playable object.
        """

        # First we check if the provided sample is a valid path.
        if os.path.exists(sample):
            if not any([sample.endswith(ext) for ext in ["mp3", "wav"]]):
                raise ValueError("Given path is not an mp3 or wav file.")
        else:
            available_samples = self.available_samples()

            sample = must_be_in_set(
                sample,
                available_samples + ["random"], "sample"
            )

            if sample == "random":
                sample = random.choice(available_samples)

            sample = os.sep.join([
                os.path.dirname(os.path.abspath(__file__)),
                "samples",
                "{}.wav".format(sample)
            ])

        self._path = sample
        self._minimum_execution_time = minimum_execution_time
        self._verbose = verbose

    @staticmethod
    def available_samples() -> List[str]:
        """Returns list with the available samples."""
        return [
            sample_name.split(".")[0]
            for sample_name in os.listdir(os.sep.join([
                os.path.dirname(os.path.abspath(__file__)),
                "samples"
            ]))
        ]

    @staticmethod
    def get_elapsed_time() -> float:
        return time() - RingBell.START_TIME

    @staticmethod
    def reset_start_time():
        RingBell.START_TIME = time()

    def has_enough_time_elapsed(self) -> bool:
        return self.get_elapsed_time() > self._minimum_execution_time

    def play(self):
        """Plays the sound."""
        if self._verbose and self.has_enough_time_elapsed():
            self.reset_start_time()
            if is_notebook():
                InvisibleAudio(path=self._path).play()
            else:
                simpleaudio.WaveObject.from_wave_file(self._path).play()

    def __call__(self):
        """Plays the sound."""
        self.play()
