from __future__ import annotations
from shared import get_dataset
from os import getenv
from itertools import combinations

dataset = get_dataset()
p2_test_case_answer: str = "34"

height = len(dataset)
width = len(dataset[0])


def add_coords(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    c1x, c1y = c1
    c2x, c2y = c2
    return (c1x + c2x, c1y + c2y)


def off_grid(pt: tuple[int, int]) -> bool:
    x, y = pt
    if x < 0 or x >= width:
        return True
    if y < 0 or y >= height:
        return True
    return False


def get_antinodes_line(c1: tuple[int, int], c2: tuple[int, int]) -> list[tuple[int, int]]:
    c1x, c1y = c1
    c2x, c2y = c2

    x_delta = c1x - c2x
    y_delta = c1y - c2y
    delta = (x_delta, y_delta)

    an_list = [c1]

    next_node = add_coords(c1, delta)

    while not off_grid(next_node):
        an_list.append(next_node)
        next_node = add_coords(next_node, delta)

    delta = (-x_delta, -y_delta)
    next_node = add_coords(c1, delta)

    while not off_grid(next_node):
        an_list.append(next_node)
        next_node = add_coords(next_node, delta)

    return an_list


def get_antinodes_type(antennas: set[tuple[int, int]]) -> list[tuple[int, int]]:
    antinodes: list[tuple[int, int]] = []

    antenna_pairs = list(combinations(antennas, 2))

    for pair in antenna_pairs:
        c1, c2 = pair
        an_line = get_antinodes_line(c1, c2)
        antinodes = antinodes + an_line

    return antinodes


antennae = {}
antinode_counter = 0

for row in range(len(dataset)):
    for col in range(len(dataset[0])):
        if dataset[row][col] != ".":
            try:
                antennae[dataset[row][col]].append((col, row))
            except KeyError:
                antennae[dataset[row][col]] = [(col, row)]


def p2() -> str:
    # Solve code here, return string to submit
    all_antinodes = []

    for char in antennae.keys():
        all_antinodes = all_antinodes + get_antinodes_type(antennae[char])

    all_antinodes = set(all_antinodes)

    return f"{len(list(set(all_antinodes)))}"


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
