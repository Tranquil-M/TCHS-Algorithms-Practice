# TCHS AERO SOFTWARE TRYOUT

## YOUR TASK
Your task is to design the movement for a ground-based robot.

## THE GRID
The robot lives on a 6x6 grid. It can only inhabit one tile at any time, and it begins in the top-left corner (0,0).
Your task is to use the provided interface to move the robot to the bottom right corner (5,5) and collect as many of the six apples as possible.

## INPUT
Your program will receive input in the form of function calls.
When you run your program, it will import the required tester modules, and send a single call to `test()`, which initializes the program. Your code will follow. During execution, you may need to use api functions to read data about the state of the board or robot. To do so, use the following:

## API
You will have access to three api functions:
move_forwards() : alias - go() : moves the robot one tile in the direction it is facing. 
turn_right() : alias - rr() : rotates the robot to the right 90 degrees.
turn_left() : alias - rl() : rotates the robot to the left 90 degrees.

And getters:
get_grid() : gets the state of the grid as a two-dimensional list. apples are represented by `o`, and walls are represented by `#`. Empty spaces are represented by `.`.
get_position() : gets the position of the robot in the form `[position_x, position_y]`. Note that the top left corner is `[0,0]` and the bottom right corner is `[5,5]`.
get_direction() : gets the direction the robot is currently facing. North is designated as `0`, East is designated as `1`, et cetera.
grade() : The `grade` function is required to receive a score, and is thus required for a valid solution. To use it, place it at the end of your program. Calling it during program execution will immediately halt the robot and the program, which can be useful to exit a bad algorithm or to mark completion. In the instant that you use `grade`, your robot's position and apple count will be captured. If the position is equal to `[5,5]`, you will receive bonus points based on the difficulty of the current tester (declared at the top of `main.py`). Then, your count of apples found will be added to your score for your final total.

## BONUS POINTS
The task comes in three difficulties that you may select from.
BASIC: No changes, collect as many apples as possible and reach the exit.
HARDER: There is now 1 "wall" on the grid that the robot must navigate around. Attempting to move into a wall will cause nothing to happen. Collect all of the apples and reach the exit.
TOUGH: There are now 6 walls. Collect at least three of the apples and reach the exit.

Brute force algorithms are discouraged. If you can solve the problem easily, push yourself to optimize your solution to use less steps. 

## FAQ
Boards are randomly generated. This includes walls and apples.
There will always be 6 apples.
The robot is guaranteed to have at least one path that collects every apple and reaches the exit.
Collaboration is allowed to the extent of "tech support". 
If you have additional questions, feel free to ask.

## ENVIRONMENT
The only provided environment is a Python3 environment. If you would like to use a different language, you may, but you will not receive instant feedback from the tester. 
If you choose to use a language other than python, syntax errors will not be held against you.
If you do not know any programming languages, or do not wish to use one, you may instead use pseudocode. If you choose this option, your solution(s) must be written on physical paper and submitted as an image.
To submit any solution, email it to `tchsaero@tcusd.net` once the time runs out or you have received a score of at least `4`.

To be considered for the TCHS Aero team, your algorithm should be able to collect at least one apple consistently and reach the exit.

Good luck.
