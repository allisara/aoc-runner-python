from __future__ import annotations
from shared import get_dataset
from os import getenv
import re


def print_grid(grid: dict):
    for row in range(HEIGHT + 2):
        row_str = ""
        for col in range(WIDTH + 2):
            row_str = row_str + grid[(col - 1, row - 1)]
        print(row_str)


def reset_steps() -> dict:
    new_steps = {}
    for row in range(HEIGHT + 2):
        for col in range(WIDTH + 2):
            new_steps[(col - 1, row - 1)] = 9999999999
    new_steps[START] = 0
    return new_steps


def get_steps_to_reach(grid: dict) -> dict:
    steps_to_reach = reset_steps()

    steps = 0
    latest_steps = [START]

    while steps_to_reach[END] > 9999999990 and len(latest_steps) > 0:
        next_steps = []
        for coord in latest_steps:
            x, y = coord
            next_coords = [(x, y-1), (x+1, y), (x, y + 1), (x-1, y)]
            for next_c in next_coords:
                if grid[next_c] != "#" and steps_to_reach[next_c] > 9999999990:
                    steps_to_reach[next_c] = steps
                    next_steps.append(next_c)
        latest_steps = next_steps
        steps += 1

    return steps_to_reach


def get_shortest_path(steps: dict) -> list[tuple[int, int]]:
    all_paths = [[END]]

    while len(all_paths) > 1:
        next_paths = []
        for path in all_paths:
            current_steps = steps[path[-1]]
            x, y = path[-1]
            next_coords = [(x, y-1), (x+1, y), (x, y + 1), (x-1, y)]
            for next_c in next_coords:
                new_path = path + [next_c]
                if next_c == START:
                    return new_path
                elif steps[next_c] == current_steps - 1:
                    next_paths.append(new_path)
        all_paths = next_paths

    return [END]


dataset = get_dataset()
p2_test_case_answer: str = "6,1"

WIDTH = 7
HEIGHT = 7
INIT_BYTES = 12
START = (0, 0)
END = (WIDTH - 1, HEIGHT - 1)

grid = {}


for row in range(HEIGHT + 2):
    for col in range(WIDTH + 2):
        if row == 0 or row == HEIGHT + 1:
            grid[(col - 1, row - 1)] = "#"
        else:
            if col == 0 or col == WIDTH + 1:
                grid[(col - 1, row - 1)] = "#"
            else:
                grid[(col - 1, row - 1)] = "."

for line in range(INIT_BYTES):
    input = re.findall(r'\d+', dataset[line])

    x = int(input[0])
    y = int(input[1])

    grid[(x, y)] = "#"

grid[START] = "S"
grid[END] = "E"


def p2() -> str:
    steps_to_reach = get_steps_to_reach(grid)

    print(get_shortest_path(steps_to_reach))

    return ""


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
