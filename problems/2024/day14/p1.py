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


dataset = get_dataset()
p1_test_case_answer: str = "12"


def p1() -> str:
    # Solve code here, return string to submit
    HEIGHT = 103
    WIDTH = 101
    STEPS = 100

    robots: list[Robot] = []

    for i in range(0, len(dataset), 4):

        robots.append(Robot(dataset[i], dataset[i+1],
                      dataset[i+2], dataset[i+3], HEIGHT, WIDTH, i))

    region_1 = 0
    region_2 = 0
    region_3 = 0
    region_4 = 0

    for robot in robots:
        robot.advance(STEPS)
        if robot.y < math.floor(HEIGHT/2):
            if robot.x < math.floor(WIDTH/2):
                region_1 += 1
                print(f"Region 1: {robot}")
            elif robot.x > WIDTH/2:
                region_2 += 1
                print(f"Region 2: {robot}")
        elif robot.y > HEIGHT/2:
            if robot.x < math.floor(WIDTH/2):
                region_3 += 1
                print(f"Region 3: {robot}")
            elif robot.x > WIDTH/2:
                region_4 += 1
                print(f"Region 4: {robot}")
        else:
            print(f"Not in region: {robot}")

    for robot in robots:
        print(robot)

    print(f"{region_1}  {region_2}  {region_3}  {region_4}")

    return f"{region_1 * region_2 * region_3 * region_4}"


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
