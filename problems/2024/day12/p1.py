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
        self.value: T = value
        self.weight = 999999999999
        self.visited = False

    def __lt__(self, other: Cell) -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"{self.value}"

    def print_cell(self):
        print(f"{self.value} ({self.x}, {self.y})")

    def reset_cell(self) -> None:
        self.visited = False


class Grid:
    def __init__(self, input: list[str]) -> None:
        self.input = input
        self.height = len(input)
        self.width = len(input[0])

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

    def get_neighbors(self, c: Cell) -> list[Cell]:
        neighbors: list[Cell] = []

        try:
            if c.y > 0:
                neighbors.append(self.cells[c.y - 1][c.x])
        except IndexError:
            pass
        try:
            neighbors.append(self.cells[c.y][c.x + 1])
        except IndexError:
            pass
        try:
            neighbors.append(self.cells[c.y + 1][c.x])
        except IndexError:
            pass
        try:
            if c.x > 0:
                neighbors.append(self.cells[c.y][c.x - 1])
        except IndexError:
            pass

        return neighbors

    def reset(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False


class Garden:
    def __init__(self, start_cell: Cell, grid: Grid) -> None:
        self.value = start_cell.value
        self.cells: list[Cell] = []
        self.cells_to_check: list[Cell] = [start_cell]
        self.edges = 0

        start_cell.visited = True

        while len(self.cells_to_check) > 0:
            current_cell = self.cells_to_check.pop()
            current_edges = 4
            all_neighbors = grid.get_neighbors(current_cell)

            for neighbor in all_neighbors:
                if neighbor.value == current_cell.value:
                    current_edges -= 1
                    if not neighbor.visited:
                        neighbor.visited = True
                        self.cells_to_check.append(neighbor)

            self.cells.append(current_cell)
            self.edges += current_edges

        # def __str__(self)->str:
        #     return f"Garden {self.value}"


dataset = get_dataset()
p1_test_case_answer: str = "1930"


def p1() -> str:
    # Solve code here, return string to submit

    grid = Grid(dataset)

    gardens = []
    answer = 0

    for row in grid.cells:
        for cell in row:
            if not cell.visited:
                new_garden = Garden(cell, grid)
                answer += len(new_garden.cells) * new_garden.edges
                gardens.append(new_garden)

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
