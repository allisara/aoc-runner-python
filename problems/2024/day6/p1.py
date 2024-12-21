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
        self.visted = False

    def __lt__(self, other: Cell) -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"{self.value}"

    def print_cell(self):
        print(f"{self.value} ({self.x}, {self.y})")


class Grid:
    def __init__(self, input: list[str]) -> None:
        self.input = input
        self.height = len(input)
        self.width = len(input[0])
        self.current_point: tuple[int, int] = (0, 0)
        self.direction = 0
        self.on_map = True
        self.cells_visited = 1

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

    def turn_right(self) -> int:
        return (self.direction + 1) % 4

    def move_guard(self):
        current_x, current_y = self.current_point
        self.cells[current_y][current_x].visted = True

        next_step = self.get_neighbor_coords(
            current_x, current_y, self.direction)
        next_x, next_y = next_step

        if self.off_grid(next_step):
            self.on_map = False
        elif self.cells[next_y][next_x].value == "#":
            self.direction = self.turn_right()
        else:
            self.current_point = next_step
            if not self.cells[next_y][next_x].visted:
                self.cells_visited += 1

    # def step(self, current_pt: tuple[int, int], direction: int, visited_cells: int) -> int:
    #     next_step = self.get_neighbor_coords(*current_pt, direction)
    #     next_col, next_row = next_step
    #     self.cells[current_pt[1]][current_pt[0]].visted = True
    #     if self.off_grid(next_step):
    #         return visited_cells
    #     elif self.cells[next_row][next_col].value == "#":
    #         new_direction = self.turn_right()
    #         return self.step(current_pt, new_direction, visited_cells)
    #     else:
    #         if not self.cells[next_row][next_col].visted:
    #             return self.step(next_step, direction, visited_cells + 1)
    #         else:
    #             return self.step(next_step, direction, visited_cells)


def get_start(grid: Grid) -> tuple[int, int]:
    for row in range(grid.height):
        for col in range(grid.width):
            if grid.cells[row][col].value == "^":
                return (col, row)
    return (-1, -1)


dataset = get_dataset()
p1_test_case_answer: str = "41"


def p1() -> str:
    # Build grid
    map_grid = Grid(dataset)

    # Find the start position and direction, change the ^ to a visited .
    map_grid.current_point = get_start(map_grid)
    start_x, start_y = map_grid.current_point
    map_grid.cells[start_y][start_x].value = "."

    # step through the grid until you reach an edge. add to a counter every time you reach an unvisited cell

    while map_grid.on_map:

        map_grid.move_guard()
        # print(map_grid.current_point)

    print("~~~~")

    answer = map_grid.cells_visited

    print(answer)

    return f"{answer}"


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
