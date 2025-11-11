# Written by Hakan Sabol of TCHS Aero

import sys
if __name__ == "__main__":
    print("\nDo not run tester.py! Nothing will be output besides this message! If you aim to test your solution, ensure it begins with a call to test() and ends with a call to grade(). Then run main.py!")
    sys.exit()

# Test generator and validator
import random
import copy
from collections import deque

DIFFICULTY : int = 0
SYMBOLS = "↑→↓←"

grid = [-1]
def get_grid() -> list:
    return grid

OBSTACLE_COUNT_BY_DIFFICULTY = (0,1,8,16)
def generate_grid() -> list:
    new_grid = [['.' for i in range(6)] for j in range(6)]

    fruit_positions = [1,2,3,4,5,10,11,12,13,14,15,20,21,22,23,24,25,30,31,32,33,34,35,40,41,42,43,44,45,50,51,52,53,54]
    while (DIFFICULTY >= 1):
        new_grid = [['.' for i in range(6)] for j in range(6)]

        for i in range(OBSTACLE_COUNT_BY_DIFFICULTY[DIFFICULTY]):
            new_obstacle = [random.randint(0,5),random.randint(0,5)]
            if new_obstacle[0] * 10 + new_obstacle[1] not in (0, 55): # invalid places (start and end)
                new_grid[new_obstacle[0]][new_obstacle[1]] = '#'

        # BFS to find a valid path to the end
        opts = [-10,10,1,-1]
        visited = set([0])
        next = deque()
        next.append(0)
        while len(next) > 0:
            a = next.popleft()
            if a % 10 == 9 or a < 0 or a % 10 > 5 or a > 55: # oob
                continue
            for b in opts: # for each dir
                cur = a + b
                if cur % 10 == 9 or cur < 0 or cur % 10 > 5 or cur > 55:  # oob
                    continue
                if cur in visited:
                    continue
                if new_grid[cur//10][cur%10] != '#':
                    visited.add(cur)
                    next.append(cur)
        # print_output = "\n".join(["".join(map(str, new_grid[i])) for i in range(6)])
        # print(print_output)
        # print(visited)
        # input()
        if 55 in visited: # valid obstacles
            # spawn fruits
            fruit_positions = list(visited)
            fruit_positions.remove(0)
            fruit_positions.remove(55)
            break

    for i in range(6):
        new_fruit = random.choice(fruit_positions)
        fruit_positions.remove(new_fruit)
        new_grid[new_fruit//10][new_fruit%10] = 'o'

    return new_grid

# ROBOT STATUS
position_x : int = 0
position_y : int = 0
step : int = 0
direction : int = 1
fruits = 0
def get_position():
    return [position_x,position_y]
def get_direction():
    return direction

halt = True
def test(diff : int = 0):
    global grid, halt, DIFFICULTY
    DIFFICULTY = diff
    halt = True
    grid = generate_grid()
    redraw()

debug_buffer = []
def redraw():
    global halt, debug_buffer

    print("\n" * 2) # console clear that doesn't delete history

    print_grid = copy.deepcopy(grid)
    print_grid[position_y][position_x] = SYMBOLS[direction]

    print_output = "Step " + str(step) + "\n"
    print_output += " Position: " + str((position_x,position_y)) + "\n"
    print_output += " Direction: " + "NESW"[direction] + "\n"
    print_output += "\n".join(["".join(map(str, print_grid[i])) for i in range(len(grid))])

    for a in debug_buffer:
        print_output += '\n'
        print_output += a
    debug_buffer = []

    print(print_output)
    if halt:
        i =input("Press enter to continue, or type 'skip' to skip to the end of execution")
        if i.lower() in ("skip", "s"):
            halt = False

MOVEMENT_VECTORS = [(0,-1),(1,0),(0,1),(-1,0)]
def move_forwards():
    global position_x,position_y, step, fruits, debug_buffer

    new_pos = (position_x + MOVEMENT_VECTORS[direction][0], position_y + MOVEMENT_VECTORS[direction][1])
    if max(new_pos) >= 6 or min(new_pos) < 0:
        debug_buffer.append("Failed to move to position: " + str(new_pos))
    else:
        if grid[new_pos[1]][new_pos[0]] == '#':
            debug_buffer.append("Hit a wall at position: " + str(new_pos))
        else:
            position_x = new_pos[0]
            position_y = new_pos[1]
            step += 1
            if grid[position_y][position_x] == 'o':
                fruits += 1
                grid[position_y][position_x] = '.'

    redraw()
def turn_right():
    global direction, step
    direction = (direction + 1) % 4
    step += 1
    redraw()
def turn_left():
    global direction, step
    direction = (direction - 1) % 4
    step += 1
    redraw()
go = move_forwards
tr = turn_right
tl = turn_left

def grade():
    # kill the program
    print()
    print("Algorithm Terminated!")
    did_win = position_x+position_y == 10
    print("Your robot reached the exit!" if did_win else "Your robot failed to reach the exit.")
    score = (3 if did_win else 0) + fruits + (4 * DIFFICULTY if did_win else 0)
    print("Score: " + str(score))
    print("win: " + str(3 if did_win else 0) + "/3" + ", apples: " + str(fruits) + "/6" + ", difficulty: " + str(4 * DIFFICULTY if did_win else 0) + "/8")

    if (score > 4):
        print("You've received at least four points. Email your solution to tchsaero@tcusd.net to submit, and/or try for more points by improving your algorithm.")
    sys.exit()
