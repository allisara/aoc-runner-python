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

    def get_neighbor_coords(self, direction: str) -> tuple[int, int] | list[tuple[int, int]]:
        directions = ["up", "down", "left", "right",
                      "up-left", "up-right", "down-left", "down-right"]

        if direction == "all":
            neighbors = []
            for item in directions:
                neighbors.append(self.get_neighbor_coords(item))
            return neighbors

        if direction == "up":
            return (self.x, self.y - 1)
        if direction == "down":
            return (self.x, self.y + 1)
        if direction == "left":
            return (self.x - 1, self.y)
        if direction == "right":
            return (self.x + 1, self.y)
        if direction == "up-left":
            return (self.x - 1, self.y - 1)
        if direction == "up-right":
            return (self.x + 1, self.y - 1)
        if direction == "down-left":
            return (self.x - 1, self.y + 1)
        if direction == "down-right":
            return (self.x + 1, self.y + 1)

        return self.xy

    # def get_neighbor_coords(self, direction: str) -> tuple[int, int]:
    #     if direction == "up":
    #         return (self.x, self.y - 1)
    #     if direction == "down":
    #         return (self.x, self.y + 1)
    #     if direction == "left":
    #         return (self.x - 1, self.y)
    #     if direction == "right":
    #         return (self.x + 1, self.y)
    #     if direction == "up-left":
    #         return (self.x - 1, self.y - 1)
    #     if direction == "up-right":
    #         return (self.x + 1, self.y - 1)
    #     if direction == "down-left":
    #         return (self.x - 1, self.y + 1)
    #     if direction == "down-right":
    #         return (self.x + 1, self.y + 1)
    #     return self.xy


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


class Garden:
    def __init__(self, start_cell: Cell, grid: Grid) -> None:
        self.value = start_cell.value
        self.cells: list[Cell] = []
        self.cells_to_check: list[Cell] = [start_cell]
        self.plot: set[tuple[int, int]] = set()
        self.padded_plot = {}
        self.edges = 0
        self.corners = 0
        self.min_x = 9999999
        self.min_y = 9999999
        self.max_x = 0
        self.max_y = 0

        start_cell.visited = True

        while len(self.cells_to_check) > 0:
            current_cell = self.cells_to_check.pop()
            current_edges = 4

            if current_cell.x < self.min_x:
                self.min_x = current_cell.x
            elif current_cell.x > self.max_x:
                self.max_x = current_cell.x

            if current_cell.y < self.min_y:
                self.min_y = current_cell.y
            elif current_cell.y > self.max_y:
                self.max_y = current_cell.y

            orth_neighbors = grid.get_neighbors(current_cell)

            for neighbor in orth_neighbors:
                if neighbor.value == current_cell.value:
                    current_edges -= 1
                    if not neighbor.visited:
                        neighbor.visited = True
                        self.cells_to_check.append(neighbor)

            self.cells.append(current_cell)
            self.plot.add(current_cell.xy)
            self.edges += current_edges

        for y in range(self.min_y-1, self.max_y + 2):
            for x in range(self.min_x - 1, self.max_x + 2):
                if (x, y) in self.plot:
                    self.padded_plot[(x, y)] = True
                else:
                    self.padded_plot[(x, y)] = False

    def __str__(self) -> str:
        s = ""
        for y in range(self.min_y-1, self.max_y + 2):
            for x in range(self.min_x - 1, self.max_x + 2):
                if self.padded_plot[(x, y)]:
                    s = s + f"{self.value}"
                else:
                    s = s + "."
            s = s + "\n"

        return s

    def count_corners(self) -> int:
        all_corners = 0
        if len(self.cells) == 1:
            return 4

        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                current = self.padded_plot[(x, y)]
                top = self.padded_plot[(x, y-1)]
                right = self.padded_plot[(x+1, y)]
                top_right = self.padded_plot[(x+1, y-1)]
                bottom_right = self.padded_plot[(x+1, y+1)]
                bottom = self.padded_plot[(x, y+1)]
                left = self.padded_plot[(x-1, y)]

                if top != current and right != current and top_right != current:
                    all_corners += 1
                if right != current and bottom != current and bottom_right != current:
                    all_corners += 1
                if bottom != current and left != current:
                    all_corners += 1
                if left != current and top != current:
                    all_corners += 1

        return all_corners

    def price(self) -> int:
        return self.count_corners() * len(self.cells)


#
dataset = get_dataset()
p2_test_case_answer: str = "1206"


def p2() -> str:
    # Solve code here, return string to submit

    grid = Grid(dataset)

    gardens: list[Garden] = []
    answer = 0

    for row in grid.cells:
        for cell in row:
            if not cell.visited:
                new_garden = Garden(cell, grid)
                answer += len(new_garden.cells) * new_garden.corners
                gardens.append(new_garden)

    for garden in gardens:
        print(garden)
        print(f"corners: {garden.count_corners()}, price: {garden.price()}")
        answer += garden.price()

    # print(gardens[0])

    return f"{answer}"

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
