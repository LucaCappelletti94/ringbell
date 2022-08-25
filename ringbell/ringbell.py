from typing import List
import os
import random
from environments_utils import is_notebook
from .utils import InvisibleAudio
from userinput.utils import must_be_in_set
import simpleaudio

__all__ = ["RingBell"]


class RingBell:

    def __init__(
        self,
        sample: str = "microwave",
        verbose: bool = True
    ):
        """Create a new RingBell.

        Parameters
        ------------------------------------------
        sample: str = "microwave"
            Name of one of the available samples.
            Currently available are 'bojack', 'pink_guy', 'rick', 'whale' and 'microwave'.
            Use 'random' for choosing a random sample.
            If the provided element is not in the set, we will check for
            a possible path.
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

    def play(self):
        """Plays the sound."""
        if self._verbose:
            if is_notebook():
                InvisibleAudio(path=self._path).play()
            else:
                simpleaudio.WaveObject.from_wave_file(self._path).play()

    def __call__(self):
        """Plays the sound."""
        self.play()
