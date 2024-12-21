from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "18"

grid = []

for line in dataset:
    new_line = []
    for c in line:
        new_line.append(c)
    grid.append(new_line)

grid_height = len(dataset)
grid_width = len(dataset[0])

# (x, y)
directions = {
    "up-left": (-1, -1),
    "up": (0, -1),
    "up-right": (1, -1),
    "right": (1, 0),
    "down-right": (1, 1),
    "down": (0, 1),
    "down-left": (-1, 1),
    "left": (-1, 0)
}


def get_neighbor_coords(coords: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    start_x, start_y = coords
    x_delta, y_delta = direction

    return (start_x + x_delta, start_y + y_delta)


def is_in_grid(coords: tuple[int, int]) -> bool:
    col, row = coords

    if col < 0 or col >= grid_width:
        return False
    if row < 0 or row >= grid_height:
        return False

    return True


def add_to_str(s: str, current_coord: tuple[int, int], direction: tuple[int, int]) -> int:
    if s == "XMAS":
        return 1
    elif len(s) >= 4:
        return 0

    next_step = get_neighbor_coords(current_coord, direction)
    new_col, new_row = next_step

    if is_in_grid(next_step):
        new_s = s + grid[new_row][new_col]
        # print(new_s)
        return add_to_str(new_s, next_step, direction)

    return 0


def count_xmases(current_coords: tuple[int, int]) -> int:
    xmases = 0

    for direction in directions.keys():
        xmases += add_to_str("X", current_coords, directions[direction])

    return xmases


def p1() -> str:
    # Solve code here, return string to submit

    answer = 0

    for row in range(grid_height):
        for col in range(grid_width):
            c = grid[row][col]
            if c == "X":
                answer += count_xmases((col, row))

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {
        'nothing' if p1_answer == '' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
