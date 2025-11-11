from tester import (
    test, move_forwards, turn_right, turn_left, go, tl, tr, grade,
    get_position, get_direction, get_grid
)

SELECT_DIFFICULTY = 0
test(SELECT_DIFFICULTY)

def apple_coords(grid) -> list:
    return [(x, y) for y, row in enumerate(grid) for x, space in enumerate(row) if space == "o"]

def find_closest_apple(apple_coordinates, x, y) -> tuple:
    if not apple_coordinates:
        return None
    return min(apple_coordinates, key=lambda a: abs(a[0] - x) + abs(a[1] - y))

def find_direction_to_move(apple_coordinate, player_coordinates) -> list:
    apple_x, apple_y = apple_coordinate
    player_x, player_y = player_coordinates
    change_in_x = apple_x - player_x
    change_in_y = apple_y - player_y
    
    directions = []
    if change_in_x != 0:
        directions.append((1 if change_in_x > 0 else 3, abs(change_in_x)))
    if change_in_y != 0:
        directions.append((2 if change_in_y > 0 else 0, abs(change_in_y)))
    return directions

def face_correct_dir(target_dir):
    current_dir = get_direction()
    diff = (target_dir - current_dir) % 4
    
    if diff == 0:
        return
    elif diff == 1:
        turn_right()
    elif diff == 2:
        turn_right()
        turn_right()
    elif diff == 3:
        turn_left()

    return

def movement(move_dir):
    for direction, steps in move_dir:
        face_correct_dir(direction)
        for _ in range(steps):
            move_forwards()

def main(debug: bool = False):
    while True:
        current_x, current_y = get_position()
        grid = get_grid()
        apples = apple_coords(grid)

        if not apples:
            target = (5, 5)
            move_dir = find_direction_to_move(target, (current_x, current_y))
            movement(move_dir)
            break

        closest_apple = find_closest_apple(apples, current_x, current_y)
        move_dir = find_direction_to_move(closest_apple, (current_x, current_y))
        movement(move_dir)

        if debug:
            print(f"Apples: {apples}", flush=True)
            print(f"Closest Apple: {closest_apple}", flush=True)
            print(f"Move Direction: {move_dir}", flush=True)
            print(f"Position: ({current_x}, {current_y})", flush=True)
            print(f"Direction: {get_direction()}", flush=True)

    grade()


if __name__ == "__main__":
    main(debug=True)
    #I don't know why but debug doesn't seem to work?? It might because of the way tester handles prints
