from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "9"

grid: list[list[str]] = []

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


def add_coords(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    c1x, c1y = c1
    c2x, c2y = c2
    return (c1x + c2x, c1y + c2y)


def get_str_at(coord: tuple[int, int]) -> str:
    return grid[coord[1]][coord[0]]


def check_x(a: tuple[int, int]) -> bool:
    s1 = get_str_at(add_coords(a, directions["up-left"])) + \
        "A" + get_str_at(add_coords(a, directions["down-right"]))
    s2 = get_str_at(add_coords(a, directions["down-left"])) + \
        "A" + get_str_at(add_coords(a, directions["up-right"]))

    return (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM")


def p2() -> str:
    # Solve code here, return string to submit
    counter = 0

    for row in range(1, grid_height - 1):
        for col in range(1, grid_width - 1):
            if grid[row][col] == "A":
                if check_x((col, row)):
                    counter += 1

    return f"{counter}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {
        'nothing' if p2_answer == '' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
