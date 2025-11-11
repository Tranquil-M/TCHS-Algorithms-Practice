# Editing these imports may result in an invalid solution.
from tester import test, move_forwards, turn_right, turn_left, go, tl, tr, grade, get_position, get_direction, get_grid

# Select the difficulty of the tester from 0 to 2.
SELECT_DIFFICULTY = 0
test(SELECT_DIFFICULTY)

'''
WRITE YOUR SOLUTION HERE.

Note the available API calls:
move_forwards() / go() : moves forwards in the direction specified by direction.
turn_right() / tr() : turns right, or clockwise. This increments direction.
turn_left() / tl() : turns left, or counter-clockwise. This decrements direction.
get_grid() -> list : Returns the state of the grid and everything on it. '.' = empty, 'o' = fruit, '#' = wall. The robot will not be included.
get_position() -> list : Returns the position of the robot as a list in the format: [position_x, position_y]
get_direction() -> int : Returns the direction the robot is facing as an int. 0: North , 1: East , 2: South , 3: West
'''

# This code serves to display valid syntax for this problem. You may safely delete everything following this except for "grade()"
grid = get_grid()
direction = get_direction()
playerX, playerY = get_position()
coordinates = []
apple_score = 0

print(playerX, playerY)

def apple_coords(grid):
    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            if space == "o":
                coordinates.append((x, y))
    return coordinates

def get_dir(direction):
    print('Direction is: (', direction, ") 0: North , 1: East , 2: South , 3: West ")

def movement():
    for coord in coordinates:
        print((playerX - coord[0]), (playerY - coord[1])) 
        distX = playerX - coord[0]
        distY = playerY - coord[1]
        


print(apple_coords(grid))
get_dir(direction)
movement()


# Your algorithm must end with a call to grade().
# Calling grade() will halt execution and print your score.
# You may call grade() at any point, but note that no operations will succeed after grade() is called.
# When grade() is called, the robot's position will be queried. If it is equal to (5,5), the "reach the end" task is successful.
# If it is called after moving away from the end, you will not receive the points for that task.
grade()
