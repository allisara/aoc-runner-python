from __future__ import annotations
from shared import get_dataset
from os import getenv
import re

dataset = get_dataset()
p1_test_case_answer: str = "22"

WIDTH = 7
HEIGHT = 7
BYTES = 12
START = (0, 0)
END = (WIDTH - 1, HEIGHT - 1)


grid = {}
steps_to_reach = {}


def print_grid(grid: dict):
    for row in range(HEIGHT + 2):
        row_str = ""
        for col in range(WIDTH + 2):
            row_str = row_str + grid[(col - 1, row - 1)]
        print(row_str)


for row in range(HEIGHT + 2):
    for col in range(WIDTH + 2):
        if row == 0 or row == HEIGHT + 1:
            grid[(col - 1, row - 1)] = "#"
        else:
            if col == 0 or col == WIDTH + 1:
                grid[(col - 1, row - 1)] = "#"
            else:
                grid[(col - 1, row - 1)] = "."
        steps_to_reach[(col - 1, row - 1)] = 9999999999

for line in range(BYTES):
    input = re.findall(r'\d+', dataset[line])

    x = int(input[0])
    y = int(input[1])

    grid[(x, y)] = "#"


def p1() -> str:
    steps = 0

    grid[START] = "S"
    grid[END] = "E"
    steps_to_reach[START] = 0

    latest_steps = [START]

    while steps_to_reach[END] > 9999999990:
        next_steps = []
        for coord in latest_steps:
            x, y = coord
            next_coords = [(x, y-1), (x+1, y), (x, y + 1), (x-1, y)]
            for next_c in next_coords:
                if grid[next_c] != "#" and steps_to_reach[next_c] > 9999999990:
                    grid[next_c] = "O"
                    steps_to_reach[next_c] = steps
                    next_steps.append(next_c)
        latest_steps = next_steps
        steps += 1

    print_grid(grid)

    return f"{steps}"


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
