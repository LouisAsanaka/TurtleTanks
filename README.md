# TurtleTanks
A 2D local multiplayer Tank game, implemented in Python turtle module

**Player 1 Keys:**

* W, A, S, D = Forward, Turn Left, Backward, Turn Right
* Space = Fire

**Player 2 Keys:**

* Up Arrow, Left Arrow, Down Arrow, Right Arrow = Forward, Turn Left, Backward, Turn Right
* Enter = Fire

The longer you hold the fire button, the farther the bullet goes.

Requires *Python 3*, and the *turtle* module should be pre-installed. Also, winsound is used, so
a Windows machine is recommended, though definitely not required.

Run the program by executing **game.py**.

Build obstacles in the **tutorial.py** file

Supported shapes:
* Square
* Rectangle
* Circle

All shapes support collision with the tanks, which have bounding boxes approximated by circles (...)
