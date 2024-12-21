from shared import get_dataset
from os import getenv
from grid import Grid

dataset = get_dataset()
p2_test_case_answer: str = "64"


class Platform(Grid):
    def __init__(self, input: list[str]) -> None:
        super().__init__(input)

    def run_cycle(self):
        # print(self)
        self.roll_up()
        # print(self)
        self.roll_left()
        # print(self)
        self.roll_down()
        # print(self)
        self.roll_right()
        # print(self)

    def roll_up(self) -> None:
        ceilings: list[int] = []
        for col in self.grid[0]:
            ceilings.append(-1)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.get_value_at_coord(x, y) == "#":
                    ceilings[x] = y
                elif self.get_value_at_coord(x, y) == "O":
                    top_empty = ceilings[x] + 1
                    # print(
                    #     f"The {self.get_value_at_coord(x, y)} at ({x}, {y}) should move to row {top_empty}")

                    self.grid[top_empty][x].value = "O"
                    ceilings[x] = top_empty
                    if y > top_empty:
                        self.grid[y][x].value = "."
                        # print(self)

        return

    def roll_left(self) -> None:
        # print("Rolling left")
        left_walls: list[int] = []
        for col in self.grid:
            left_walls.append(-1)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.get_value_at_coord(x, y) == "#":
                    left_walls[y] = x
                elif self.get_value_at_coord(x, y) == "O":
                    leftest_empty = left_walls[y] + 1
                    # print(
                    #     f"The {self.get_value_at_coord(x, y)} at ({x}, {y}) should move to row {top_empty}")

                    self.grid[y][leftest_empty].value = "O"
                    left_walls[y] = leftest_empty
                    if x > leftest_empty:
                        self.grid[y][x].value = "."
                        # print(self)
        return

    def roll_down(self) -> None:
        # print("Rolling down")
        floors: list[int] = []
        for col in self.grid[0]:
            floors.append(len(self.grid))

        for y in range(len(self.grid) - 1, -1, -1):
            for x in range(len(self.grid[0])):
                if self.get_value_at_coord(x, y) == "#":
                    floors[x] = y
                elif self.get_value_at_coord(x, y) == "O":
                    bottom_empty = floors[x] - 1
                    # print(
                    #     f"The {self.get_value_at_coord(x, y)} at ({x}, {y}) should move to row {top_empty}")

                    self.grid[bottom_empty][x].value = "O"
                    floors[x] = bottom_empty
                    if y < bottom_empty:
                        self.grid[y][x].value = "."
                        # print(self)
        return

    def roll_right(self) -> None:
        # print("Rolling right")
        right_walls: list[int] = []
        for col in self.grid:
            right_walls.append(len(self.grid[0]))

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0]) - 1, -1, -1):
                if self.get_value_at_coord(x, y) == "#":
                    right_walls[y] = x
                elif self.get_value_at_coord(x, y) == "O":
                    rightest_empty = right_walls[y] - 1
                    # print(
                    #     f"The {self.get_value_at_coord(x, y)} at ({x}, {y}) should move to row {top_empty}")

                    self.grid[y][rightest_empty].value = "O"
                    right_walls[y] = rightest_empty
                    if x < rightest_empty:
                        self.grid[y][x].value = "."
                        # print(self)
        return

    def get_score(self) -> int:
        weight = 0
        weight_in_row = len(self.grid)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.get_value_at_coord(x, y) == "O":
                    weight += weight_in_row
                    # print(weight)
            weight_in_row -= 1

        return weight


def p2() -> str:
    # Solve code here, return string to submit
    platform = Platform(dataset)

    # for i in range(1000):
    #     platform.run_cycle()

    for i in range(1000):
        platform.run_cycle()
        if i > 900:
            print(f"{i}: {platform.get_score()}")

    # print((1000000000 - 2) % 7)

    # # print(platform)

    # platform.roll_up()

    # print(platform)

    print(1000000000 % 7)

    print(986 % 7)

    answer = platform.get_score()

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {'nothing' if p2_answer=='' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
