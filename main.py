from tester import (
    test,
    move_forwards,
    turn_right,
    turn_left,
    grade,
    get_position,
    get_direction,
    get_grid,
)
import heapq

SELECT_DIFFICULTY = 3
test(SELECT_DIFFICULTY)


def apple_coords(grid):
    return [(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "o"]


def neighbors(x, y, grid):
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    valid_neighbors = []
    for dir_x, dir_y in offsets:
        actual_x, actual_y = x + dir_x, y + dir_y
        if (
            0 <= actual_y < len(grid)
            and 0 <= actual_x < len(grid[0])
            and grid[actual_y][actual_x] != "#"
        ):
            valid_neighbors.append((actual_x, actual_y))
    return valid_neighbors


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for n in neighbors(*current, grid):
            temp_g = g_score[current] + 1
            if temp_g < g_score.get(n, float("inf")):
                came_from[n] = current
                g_score[n] = temp_g
                f = temp_g + heuristic(n, goal)
                heapq.heappush(open_set, (f, n))


def face_correct_dir(target_dir):
    current_dir = get_direction()
    diff = (target_dir - current_dir) % 4
    if diff == 1:
        turn_right()
    elif diff == 2:
        turn_right()
        turn_right()
    elif diff == 3:
        turn_left()


def move_toward_path(path):
    for next_x, next_y in path:
        player_x, player_y = get_position()
        horizontal_dir, vertical_dir = next_x - player_x, next_y - player_y
        if horizontal_dir == 1:
            face_correct_dir(1)
        elif horizontal_dir == -1:
            face_correct_dir(3)
        elif vertical_dir == 1:
            face_correct_dir(2)
        elif vertical_dir == -1:
            face_correct_dir(0)
        move_forwards()


def main():
    while True:
        x, y = get_position()
        grid = get_grid()
        apples = apple_coords(grid)
        if not apples:
            path = astar(grid, (x, y), (5, 5))
            move_toward_path(path)
            break
        apples.sort(key=lambda a: (heuristic((x, y), a)))
        target = apples[0]
        path = astar(grid, (x, y), target)
        if not path:
            break
        move_toward_path(path)

    grade()


if __name__ == "__main__":
    main()
