from IPython.display import Audio, display

__all__ = ["InvisibleAudio"]


class InvisibleAudio(Audio):
    def __init__(self, path: str):
        """Return invisible audio object for jupyter notebook.
        
        Parameters
        -----------------------------
        path: str,
            the path to the file to be used.

        Returns
        ------------------------------
        New InvisibleAudio object.
        """
        super().__init__(
            filename=path,
            autoplay=True
        )

    def _repr_html_(self):
        """Return html representation for the invisible audio."""
        audio = super()._repr_html_()
        audio = audio.replace(
            '<audio', '<audio onended="this.parentNode.removeChild(this)"')
        return '<div style="display:none">{audio}</div>'.format(
            audio=audio
        )

    def play(self):
        """Displays the object, hence playing it."""
        display(self)
