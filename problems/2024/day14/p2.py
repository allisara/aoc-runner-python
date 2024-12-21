from __future__ import annotations
from shared import get_dataset
from os import getenv
import math


class Robot:
    def __init__(self, x: int, y: int, xv: int, yv: int, height: int, width: int, id: int) -> None:
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.height = height
        self.width = width
        self.id = id

    def __str__(self) -> str:
        return f"({self.x}, {self.y}): xv = {self.xv}, yv = {self.yv}"

    def advance(self, seconds: int):
        self.x = (self.x + self.xv * seconds) % self.width
        self.y = (self.y + self.yv * seconds) % self.height


def get_grid_str(robots: list[Robot], height: int, width: int, step: int) -> str:
    grid: list[list[str]] = []

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(" ")
        grid.append(row)

    for r in robots:
        grid[r.y][r.x] = "#"

    grid_str = f"Step {step}:\n"

    for y in range(height):
        for x in range(width):
            grid_str = grid_str + grid[y][x]
        grid_str = grid_str + "\n"

    return grid_str


dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p2() -> str:
    # Solve code here, return string to submit
    HEIGHT = 103
    WIDTH = 101
    STEPS = 10000

    robots: list[Robot] = []

    for i in range(0, len(dataset), 4):

        robots.append(Robot(dataset[i], dataset[i+1],
                      dataset[i+2], dataset[i+3], HEIGHT, WIDTH, i))

    for i in range(STEPS):
        frame = get_grid_str(robots, HEIGHT, WIDTH, i)
        if "##########" in frame:
            print(frame)
        for r in robots:
            r.advance(1)

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
