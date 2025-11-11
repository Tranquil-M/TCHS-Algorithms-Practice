# Editing these imports may result in an invalid solution.
from tester import test, move_forwards, turn_right, turn_left, go, tl, tr, grade, get_position, get_direction, get_grid
import math 

# Select the difficulty of the tester from 0 to 2.
SELECT_DIFFICULTY = 0
test(SELECT_DIFFICULTY)
# WRITE YOUR SOLUTION HERE.

# Note the available API calls:
# move_forwards() / go() : moves forwards in the direction specified by direction.
# turn_right() / tr() : turns right, or clockwise. This increments direction.
# turn_left() / tl() : turns left, or counter-clockwise. This decrements direction.
# get_grid() -> list : Returns the state of the grid and everything on it. '.' = empty, 'o' = fruit, '#' = wall. The robot will not be included.
# get_position() -> list : Returns the position of the robot as a list in the format: [position_x, position_y]
# get_direction() -> int : Returns the direction the robot is facing as an int. 0: North , 1: East , 2: South , 3: West

def apple_coords(grid) -> list:

    coordinates: list = []
    for y, row in enumerate(grid):
        print(row)
        for x, space in enumerate(row):
            if space == "o":
                coordinates.append((x, y))
    

    return coordinates

def find_closest_apple(apple_coordinates, x, y) -> tuple:
    
    apple_mag_distances: dict = {}
    for apple in apple_coordinates:
        x2 = apple[0]
        y2 = apple[1]
        dx_squared = (x2 - x)**2
        dy_squared = (y2 - y)**2
        distance = math.sqrt(dx_squared + dy_squared)
        apple_mag_distances[apple] = distance
        

    lowest_mag = sorted(apple_mag_distances.items())[0]
    closest_apple: tuple = lowest_mag[0]
    print('apple mag dist: ', apple_mag_distances)
    return closest_apple

def find_direction_to_move(apple_coordinate, player_coordinates) -> list:
    apple_x, apple_y = apple_coordinate
    player_x, player_y = player_coordinates
    change_in_x = apple_x - player_x
    change_in_y = apple_y - player_y
    
    if change_in_x < 0:
        direction_x_quantity = (3, abs(change_in_x))
    else:
        direction_x_quantity = (1, abs(change_in_x))
    
    if change_in_y < 0:
        direction_y_quantity = (0, abs(change_in_y))
    else:
        direction_y_quantity = (2, abs(change_in_y))

    direction: list = [direction_x_quantity, direction_y_quantity]
    return direction

def face_correct_dir(target_dir):
    while True:
        current_dir = get_direction()
        if current_dir == target_dir:
            break
        turn_left()  
    return "facing right way"


def movement(PlayerX, PlayerY, apple_coords,move_dir):
    appleX, appleY = apple_coords
    face_correct_dir(move_dir[0][0])
    for i in range(move_dir[0][1]):
        move_forwards()

    face_correct_dir(move_dir[1][0])
    for i in range(move_dir[1][1]):
        move_forwards()



def main():
    while True:
        current_x, current_y = get_position()
        current_dir = get_direction()
        grid = get_grid()
        apple_coordinates = apple_coords(grid)
        if not len(apple_coordinates):
            movement(current_x, current_y,(5,5), find_direction_to_move( (5,5), (current_x, current_y) ))
            break

        closest_apple = find_closest_apple(apple_coordinates, current_x, current_y)
        move_direction = find_direction_to_move(closest_apple, (current_x, current_y))
        movement(current_x, current_y, closest_apple, move_direction)
        print(f"Apple Coordinates: {apple_coordinates}")
        print(f"Closest Apple: {closest_apple}")
        print(f"Move Direction: {move_direction}")
        print(f"Current Direction: {current_dir}")
        print(f"Current X: {current_x}")
        print(f"Current Y: {current_y}")

        
        
# Your algorithm must end with a call to grade().
# Calling grade() will halt execution and print your score.
# You may call grade() at any point, but note that no operations will succeed after grade() is called.
# When grade() is called, the robot's position will be queried. If it is equal to (5,5), the "reach the end" task is successful.
# If it is called after moving away from the end, you will not receive the points for that task.

if __name__ == "__main__":
    main()

grade()
