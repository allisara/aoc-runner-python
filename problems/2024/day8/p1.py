from __future__ import annotations
from shared import get_dataset
from os import getenv
from itertools import combinations

dataset = get_dataset()
p1_test_case_answer: str = "14"

height = len(dataset)
width = len(dataset[0])


def get_antinodes_pair(c1: tuple[int, int], c2: tuple[int, int]) -> list[tuple[int, int]]:
    c1x, c1y = c1
    c2x, c2y = c2

    x_delta = c1x - c2x
    y_delta = c1y - c2y

    an1 = (c1x + x_delta, c1y + y_delta)
    an2 = (c2x - x_delta, c2y - y_delta)

    return [an1, an2]


def off_grid(pt: tuple[int, int]) -> bool:
    x, y = pt
    if x < 0 or x >= width:
        return True
    if y < 0 or y >= height:
        return True
    return False


def get_antinodes_type(antennas: set[tuple[int, int]]) -> list[tuple[int, int]]:
    antinodes: list[tuple[int, int]] = []

    antenna_pairs = list(combinations(antennas, 2))

    for pair in antenna_pairs:
        a1, a2 = get_antinodes_pair(*pair)
        if not off_grid(a1):
            antinodes.append(a1)
        if not off_grid(a2):
            antinodes.append(a2)

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


def p1() -> str:
    # Solve code here, return string to submit
    # test = {(4, 3), (6, 5), (8, 4)}

    # get_antinodes_type(test)
    all_antinodes = []

    for char in antennae.keys():
        all_antinodes = all_antinodes + get_antinodes_type(antennae[char])

    print(len(all_antinodes))

    all_antinodes = set(all_antinodes)

    return f"{len(list(set(all_antinodes)))}"


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
