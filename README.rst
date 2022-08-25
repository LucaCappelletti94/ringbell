Ding
=========================================================================================
|pip| |downloads|

Python package for playing a sound when a task is complete. The callbacks additionally works also within jupyter notebook,
so that if you are working on a notebook on a remote machine it plays the audio within your browser and not in the server.

How do I install this package?
----------------------------------------------
You will need a couple packages that you might not already have installed:

.. code:: shell

    sudo apt install python3-dev
    sudo apt install libasound2-dev

Finally as usual, just download it using pip:

.. code:: shell

    pip install ding


Usage examples
-----------------------------------------------
It's quite trivia, really, just go:

.. code:: python

    from ding import Ding

    def my_long_task():
        # Do stuf...

        # And when it is finished...
        Ding()


What abount a custom sound? Just pass it as an argument.

.. code:: python

    from ding import Ding

    def my_long_task():
        # Do stuf...

        # And when it is finished...
        Ding(path="my_custom_sound.mp3")


.. |pip| image:: https://badge.fury.io/py/ding.svg
    :target: https://badge.fury.io/py/ding
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/ding
    :target: https://pepy.tech/badge/ding
    :alt: Pypi total project downloads 
