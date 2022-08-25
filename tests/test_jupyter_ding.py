from ding import Ding
from ding.utils import InvisibleAudio


def test_invisible_audio():
    InvisibleAudio(Ding()._path).play()
    InvisibleAudio(Ding()._path)._repr_html_()
    InvisibleAudio(Ding("random")._path)._repr_html_()
    for sample in Ding.available_samples():
        InvisibleAudio(Ding(sample)._path).play()