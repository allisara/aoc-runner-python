from shared import get_dataset
from os import getenv

from grid import Grid

dataset = get_dataset()
p1_test_case_answer: str = "136"


class Platform(Grid):
    def __init__(self, input: list[str]) -> None:
        super().__init__(input)

    def roll_up(self) -> int:
        weight = 0
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

                    weight += len(self.grid) - top_empty

        return weight

    # def get_weight(self) -> int:
    #     weight = 0

    #     for

    #     return weight


def p1() -> str:
    # Solve code here, return string to submit
    answer = 0

    platform = Platform(dataset)

    print(platform)
    answer = platform.roll_up()

    print(platform)

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
