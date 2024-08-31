# audiolookback
This program creates a simple graphical user interface for controlling audio loopbacks in Python.

How it works:

User interface:

The program creates a window with a "Start" and "Stop" button.

Pressing "Start" starts the audio transmission from the microphone to the speakers.

Pressing "Stop" stops the audio transmission.

Audio loop:

The audio transmission is done in a separate thread (threading.Thread), which allows for simultaneous use of the user interface.
Closing the application:

The on_closing function ensures that audio streams are closed properly and PyAudio is terminated before the application closes.
