from __future__ import annotations
from shared import get_dataset
from os import getenv
from typing import TypeVar, Generic

T = TypeVar("T")


class Cell(Generic[T]):
    def __init__(self, x: int, y: int, value: T) -> None:
        self.x = x
        self.y = y
        self.xy = (x, y)
        self.value = value
        self.weight = 999999999999
        self.visited = [False, False, False, False]

    def __lt__(self, other: Cell) -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"{self.value}"

    def print_cell(self):
        print(f"{self.value} ({self.x}, {self.y})")

    def was_visited(self) -> bool:
        for direction in self.visited:
            if direction:
                return True
        return False

    def reset_cell(self) -> None:
        self.visited = [False, False, False, False]
        if self.value == "X":
            self.value = "."


class Grid:
    def __init__(self, input: list[str]) -> None:
        self.input = input
        self.height = len(input)
        self.width = len(input[0])
        self.current_point: tuple[int, int] = (0, 0)
        self.direction = 0
        self.on_map = True
        self.not_on_loop = True

        self.cells = self.create_cells()

    def reset(self):
        self.direction = 0
        self.on_map = True
        self.not_on_loop = True

        # for row in range(self.height):
        #     for col in range(row):
        #         self.cells[row][col].reset_cell()

        for row in range(self.height):
            for col in range(row):
                self.cells[row][col].visited = [False, False, False, False]
                if self.cells[row][col].value == "X":
                    self.cells[row][col].value = "."

    def create_cells(self) -> list[list[Cell]]:

        grid_input = []

        for row in range(len(self.input)):
            row_cells = []
            for col in range(len(self.input[0])):
                new_cell = Cell(col, row, self.input[row][col])
                row_cells.append(new_cell)
            grid_input.append(row_cells)

        return grid_input

    def __str__(self) -> str:
        grid_str = ""
        for row in self.cells:
            line_str = ""
            for cell in row:
                line_str += str(cell.value) + " "
            grid_str += line_str + "\n"
        return grid_str

    def off_grid(self, start_pt: tuple[int, int]) -> bool:
        x, y = start_pt
        if x < 0 or x >= self.width:
            return True
        if y < 0 or y >= self.height:
            return True
        return False

    def get_neighbor_coords(self, x: int, y: int, dir: int) -> tuple[int, int]:
        if dir % 2 == 0:
            y_delta = dir - 1
            return (x, y + y_delta)
        else:
            x_delta = 2 - dir
            return (x + x_delta, y)

    def turn_right(self) -> int:
        return (self.direction + 1) % 4

    def move_guard(self):
        current_x, current_y = self.current_point
        self.cells[current_y][current_x].visited[self.direction] = True
        self.cells[current_y][current_x].value = "x"

        next_step = self.get_neighbor_coords(
            current_x, current_y, self.direction)
        next_x, next_y = next_step

        if self.off_grid(next_step):
            self.on_map = False
            print("Guard left map")
        elif self.cells[next_y][next_x].value == "#":
            self.direction = self.turn_right()
            print("Guard turned right")
        elif self.cells[next_y][next_x].visited[self.direction]:
            self.not_on_loop = False
            print("Guard has been there before")
        else:
            self.current_point = next_step
            print(f"{self.__str__()}")
            print("---")

    def path_loops(self) -> bool:
        while self.on_map and self.not_on_loop:
            self.move_guard()
        print("done checking loop")
        print(f"{self.__str__()}")
        print("~~~~~~~~")
        return not self.not_on_loop


def get_start(grid: Grid) -> tuple[int, int]:
    for row in range(grid.height):
        for col in range(grid.width):
            if grid.cells[row][col].value == "^":
                return (col, row)
    return (-1, -1)


dataset = get_dataset()
p2_test_case_answer: str = "6"

test_grid = ["......",
             ".#.##.",
             ".#^.#.",
             ".####.",
             "......"]


def p2() -> str:

    small_grid = Grid(test_grid)

    print(small_grid)
    print("-------")

    small_grid.cells[0][0].value = "X"

    print(small_grid)
    print("-------")

    small_grid.reset()
    print(small_grid)

    # map_grid = Grid(test_grid)
    # st_pt = get_start(map_grid)
    # answer = 0

    # for row in range(map_grid.height):
    #     for col in range(map_grid.width):
    #         map_grid.current_point = st_pt
    #         if map_grid.cells[row][col].value == ".":

    #             map_grid.cells[row][col].value = "#"

    #             if map_grid.path_loops():
    #                 answer += 1

    #             map_grid.cells[row][col].value = "."
    #         map_grid.reset()
    #         print("--------")

    # return f"{answer}"
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
