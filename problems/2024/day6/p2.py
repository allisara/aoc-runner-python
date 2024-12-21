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
        # self.current_point: tuple[int, int] = (0, 0)
        # self.direction = 0
        # self.on_map = True
        # self.not_on_loop = True

        self.cells = self.create_cells()

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

    def find_blocker(self, st_pt: tuple[int, int], direction: int) -> tuple[int, int]:
        next_step = self.get_neighbor_coords(*st_pt, direction)
        next_x, next_y = next_step
        if self.off_grid(next_step):
            return (-1, -1)
        if self.cells[next_y][next_x].value == "#":
            return st_pt
        return self.find_blocker(next_step, direction)


def turn_right(start_dir) -> int:
    return (start_dir + 1) % 4


def get_start(grid: Grid) -> tuple[int, int]:
    for row in range(grid.height):
        for col in range(grid.width):
            if grid.cells[row][col].value == "^":
                return (col, row)
    return (-1, -1)


def is_loop(st_pt: tuple[int, int], direction: int, grid: Grid, turn_pts: set[tuple[int, int]]) -> bool:
    next_stop = grid.find_blocker(st_pt, direction)
    if next_stop == (-1, -1):
        return False
    if next_stop in turn_pts:
        return True

    turn_pts.add(next_stop)
    new_dir = turn_right(direction)
    rt_x, rt_y = grid.get_neighbor_coords(*next_stop, new_dir)
    if grid.cells[rt_y][rt_x].value == "#":
        new_dir = turn_right(new_dir)

    return is_loop(next_stop, new_dir, grid, turn_pts)


dataset = get_dataset()
p2_test_case_answer: str = "6"

test_grid_1 = ["......",
               ".#.##.",
               ".#^.#.",
               ".####.",
               "......"]

test_grid_2 = [".#..",
               "....",
               ".^.."]


def p2() -> str:

    grid = Grid(dataset)
    start = get_start(grid)
    loop_counter = 0

    for row in range(grid.height):
        for col in range(grid.width):
            if grid.cells[row][col].value == ".":
                grid.cells[row][col].value = "#"
                corners: set[tuple[int, int]] = set()
                if is_loop(start, 0, grid, corners):
                    loop_counter += 1

                grid.cells[row][col].value = "."

    print(is_loop(start, 0, grid, corners))

    grid.cells[0][2].value = "#"
    corners = set()

    print(is_loop(start, 0, grid, corners))

    return f"{loop_counter}"


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
