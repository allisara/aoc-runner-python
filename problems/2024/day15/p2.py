from __future__ import annotations
from shared import get_dataset
from os import getenv
from p1 import Cell


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

    def get_neighbor(self, current: Cell, direction: str) -> Cell:
        if direction == "up" or direction == "^":
            if current.y > 0:
                return self.cells[current.y - 1][current.x]
        if direction == "left" or direction == "<":
            if current.x > 0:
                return self.cells[current.y][current.x-1]
        if direction == "down" or direction == "v":
            return self.cells[current.y + 1][current.x]
        if direction == "right" or direction == ">":
            return self.cells[current.y][current.x + 1]
        return current

    def get_shape(self, st_pt: Cell, direction: str) -> set[Cell]:
        shape: set[Cell] = set()
        cells_to_check = set([st_pt])

        while len(cells_to_check) > 0:
            current = cells_to_check.pop()
            shape.add(current)
            next = self.get_neighbor(current, direction)

            if next.value == "[":
                cells_to_check.add(next)
                cells_to_check.add(self.get_neighbor(next, ">"))
            if next.value == "]":
                cells_to_check.add(next)
                cells_to_check.add(self.get_neighbor(next, "<"))
        return shape

    def is_moveable_shape(self, pushed_points: set[Cell], direction: str) -> bool:
        for cell in pushed_points:
            next_cell = self.get_neighbor(cell, direction)
            if next_cell.value == "#":
                return False
        return True

    def move_shape(self, shape: set[Cell], direction: str):
        cells = list(shape)
        max = 0
        min = 9999

        for cell in cells:
            if cell.y > max:
                max = cell.y
            elif cell.y < min:
                min = cell.y

        if direction == "^":
            for y in range(min - 1, max + 1):
                for cell in cells:
                    if cell.y == y:
                        self.move(cell, "^")
        elif direction == "v":
            for y in range(max + 1, min - 1, -1):
                for cell in cells:
                    if cell.y == y:
                        self.move(cell, "v")

    def move(self, c: Cell, direction: str):
        next_cell = self.get_neighbor(c, direction)
        if next_cell.value == "#":
            pass
        elif next_cell.value == ".":
            next_cell.value = c.value
            if next_cell.value == "@":
                self.robot = next_cell
            c.value = "."

        elif next_cell.value == "[" or next_cell.value == "]" or next_cell.value == "@":
            if direction == "<" or direction == ">":
                self.move(next_cell, direction)
                if next_cell.value == ".":
                    next_cell.value = c.value
                    if next_cell.value == "@":
                        self.robot = next_cell
                    c.value = "."
            else:
                shape = self.get_shape(c, direction)
                if self.is_moveable_shape(shape, direction):
                    self.move_shape(shape, direction)


dataset = get_dataset()
p2_test_case_answer: str = "9021"

commands = dataset[1]
expanded_grid: list[str] = []

for row in dataset[0]:
    new_row = ""
    for c in row:
        if c == "#":
            new_row = new_row + "##"
        elif c == "O":
            new_row = new_row + "[]"
        elif c == ".":
            new_row = new_row + ".."
        elif c == "@":
            new_row = new_row + "@."
    expanded_grid.append(new_row)

grid = Grid(expanded_grid)


def p2() -> str:

    for c in commands:
        # print(grid)
        grid.move(grid.robot, c)
        # print(c)

    print(grid)

    answer = 0

    for y in range(grid.height):
        for x in range(grid.width):
            if grid.cells[y][x].value == "[":
                answer += 100 * y + x

    return f"{answer}"
# 1448749 was too high


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
