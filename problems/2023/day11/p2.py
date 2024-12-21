from shared import get_dataset
from os import getenv
from grid import Grid, Point

dataset = get_dataset()
p2_test_case_answer: str = "8140"


class Galaxy_map(Grid):
    def __init__(self, input: list[str]) -> None:
        super().__init__(input)

        self.galaxies_unexpanded = []
        self.empty_rows = []
        self.empty_cols = []
        self.galaxies_expanded = []

        for i in range(len(self.grid)):
            self.empty_rows.append(i)
        for i in range(len(self.grid[0])):
            self.empty_cols.append(i)

        for row in self.grid:
            for point in row:
                if point.value == "#":
                    self.galaxies_unexpanded.append(point.get_coords())
                    if point.x in self.empty_cols:
                        self.empty_cols.remove(point.x)
                    if point.y in self.empty_rows:
                        self.empty_rows.remove(point.y)

        self.expand_galaxies()

    def expand_galaxies(self) -> None:

        for galaxy in self.galaxies_unexpanded:
            x, y = galaxy
            x_buffer = self.get_col_buffer(x)
            y_buffer = self.get_row_buffer(y)
            self.galaxies_expanded.append((x + x_buffer, y + y_buffer))

        return

    def get_row_buffer(self, y: int) -> int:
        buffer = 0

        for row in self.empty_rows:
            if y > row:
                buffer += 1000000 - 1

        return buffer

    def get_col_buffer(self, x: int) -> int:
        buffer = 0

        for col in self.empty_cols:
            if x > col:
                buffer += 1000000 - 1

        return buffer

    def get_answer(self) -> int:

        answer = 0

        for i in range(len(self.galaxies_expanded)):
            gal_a = self.galaxies_expanded[i]
            for j in range(i+1, len(self.galaxies_expanded)):
                gal_b = self.galaxies_expanded[j]
                answer += self.get_manhattan_distance(gal_a, gal_b)

        return answer


def p2() -> str:
    # Solve code here, return string to submit

    galaxy_map = Galaxy_map(dataset)

    # print(galaxy_map.galaxies_unexpanded)
    # print(galaxy_map.galaxies_expanded)

    answer = galaxy_map.get_answer()

    print(answer)

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
