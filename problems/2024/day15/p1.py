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
        self.robot: Cell

        self.cells = self.create_cells()

    def create_cells(self) -> list[list[Cell]]:

        grid_input = []

        for row in range(len(self.input)):
            row_cells = []
            for col in range(len(self.input[0])):
                new_cell = Cell(col, row, self.input[row][col])
                row_cells.append(new_cell)
                if new_cell.value == "@":
                    self.robot = new_cell

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

    def get_orth_neighbors(self, c: Cell) -> list[Cell]:
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

    def get_diagonal_neighbors(self, c: Cell) -> list[Cell]:
        neighbors: list[Cell] = []

        try:
            if c.y > 0 and c.x > 0:
                neighbors.append(self.cells[c.y - 1][c.x - 1])
        except IndexError:
            pass
        try:
            if c.y > 0:
                neighbors.append(self.cells[c.y - 1][c.x + 1])
        except IndexError:
            pass
        try:
            if c.x > 0:
                neighbors.append(self.cells[c.y + 1][c.x - 1])
        except IndexError:
            pass
        try:
            neighbors.append(self.cells[c.y + 1][c.x + 1])
        except IndexError:
            pass

        return neighbors

    def reset(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def get_neighbor(self, current: Cell, direction: str) -> Cell | None:
        if direction == "up" or direction == "^":
            try:
                if current.y > 0:
                    return self.cells[current.y - 1][current.x]
                else:
                    return None
            except IndexError:
                return None
        if direction == "left" or direction == "<":
            try:
                if current.x > 0:
                    return self.cells[current.y][current.x-1]
                else:
                    return None
            except IndexError:
                return None
        if direction == "down" or direction == "v":
            try:
                return self.cells[current.y + 1][current.x]
            except IndexError:
                return None
        if direction == "right" or direction == ">":
            try:
                return self.cells[current.y][current.x + 1]
            except IndexError:
                return None

    def move(self, c: Cell, direction: str):
        next_cell = self.get_neighbor(c, direction)
        if next_cell == None or next_cell.value == "#":
            pass
        elif next_cell.value == ".":
            next_cell.value = c.value
            if next_cell.value == "@":
                self.robot = next_cell
            c.value = "."

        elif next_cell.value == "O":
            self.move(next_cell, direction)
            if next_cell.value == ".":
                next_cell.value = c.value
                if next_cell.value == "@":
                    self.robot = next_cell
                c.value = "."


dataset = get_dataset()
p1_test_case_answer: str = "10092"

grid = Grid(dataset[0])
commands = dataset[1]


def p1() -> str:
    # Solve code here, return string to submit

    for c in commands:
        grid.move(grid.robot, c)

    print(grid)

    answer = 0

    for y in range(grid.height):
        for x in range(grid.width):
            if grid.cells[y][x].value == "O":
                answer += 100 * y + x

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
