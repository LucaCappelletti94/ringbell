Ring Bell
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

    pip install ringbell


Support my work ❤️
------------------------------------------------------
If you have enjoyed my work, and possibly it has saved you some precious minutes,
please do `support me on GitHub ❤️ <https://github.com/sponsors/LucaCappelletti94>`_


Integration with exceptions and Jupyter Notebooks
------------------------------------------------------
In Jupyter Notebooks it is now possible to integrate Ringbell with a one liner, that will play
a positive sound when the execution completes successfully and a negative sound when the execution
crashes and burns.

Analogous support is added for normal scripts, but only for exceptions since I am not aware of
an hook event for the end of a script.

Notification after at least one minute of execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Since in most Jupyter Notebooks, expecially for experiments, there will be a few very quick
cells and then some very long ones, we do not want to spam the user with sounds. The only
case where we'd like to advise the user is when enought time has passed since the start of either
the script execution or, in case of Jupyter Notebooks, the start of the cell execution.

To do this, simply import the ringbell package as such:

.. code:: python

    import ringbell.auto


Immediate notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you'd like to have an immediate notification for each cell and exception.

.. code:: python

    import ringbell.immediate


All exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you'd like to have an immediate notification for all exceptions.

.. code:: python

    import ringbell.all_exceptions


Custom time interval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can also customize the time interval as such:

.. code:: python

    from ringbell import auto_ringbell
    auto_ringbell(
        minimum_execution_time = 60,
        only_exceptions = False,
        good_sound="sample_for_nominal_execution",
        bad_sound="sample_for_exceptions"
    )


Usage examples
------------------------------------------------------
It's quite trivia, really, just go:

.. code:: python

    from ringbell import RingBell

    def my_long_task():
        # Do stuf...

        # And when it is finished...
        RingBell(
            sample = "microwave",
            minimum_execution_time = 0,
            verbose = True
        )


How many sounds are there? Well, just list them:

.. code:: python

    from ringbell import RingBell

    print(RingBell.available_samples())


What abount a custom sound? Just pass it as an argument.

.. code:: python

    from ringbell import RingBell

    def my_long_task():
        # Do stuf...

        # And when it is finished...
        RingBell(path="path/to/my_custom_sound.mp3")


.. |pip| image:: https://badge.fury.io/py/ringbell.svg
    :target: https://badge.fury.io/py/ringbell
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/ringbell
    :target: https://pepy.tech/badge/ringbell
    :alt: Pypi total project downloads 
