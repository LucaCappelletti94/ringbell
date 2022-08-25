from ringbell import RingBell
from ringbell.utils import InvisibleAudio


def test_invisible_audio():
    InvisibleAudio(RingBell()._path).play()
    InvisibleAudio(RingBell()._path)._repr_html_()
    InvisibleAudio(RingBell("random")._path)._repr_html_()
    for sample in RingBell.available_samples():
        InvisibleAudio(RingBell(sample)._path).play()