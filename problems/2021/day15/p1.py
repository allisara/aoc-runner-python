from __future__ import annotations
from shared import get_dataset
from os import getenv
import math
from typing import TypeVar, Generic
import heapq

T = TypeVar("T")

dataset = get_dataset()
p1_test_case_answer: str = "40"


class Cell(Generic[T]):
    def __init__(self, x: int, y: int, value: T) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.weight = math.inf

        # self.neighboring_coords = [(x-1, y-1), (x, y-1), (x + 1, y - 1),
        #                   (x-1, y), (x + 1, y),
        #                   (x-1, y+1), (x, y+1), (x + 1, y + 1)]

    def __lt__(self, other: Cell) -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"{self.value} ({self.x}, {self.y})"


class Grid:
    def __init__(self, input: list[str]) -> None:
        self.input = input
        self.height = len(input)
        self.width = len(input[0])

        self.cells = self.create_cells()

        self.cells[0][0].weight = 0
        self.cells_to_check = [self.cells[0][0]]
        heapq.heapify(self.cells_to_check)

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
                line_str += str(cell.value) + ", "
            grid_str += line_str + "\n"
        return grid_str

    def get_up_neighbor(self, cell: Cell) -> Cell | None:

        new_row = cell.y - 1
        new_col = cell.x

        if new_row >= 0:
            return self.cells[new_row][new_col]
        else:
            return None

    def get_down_neighbor(self, cell: Cell) -> Cell | None:

        new_row = cell.y + 1
        new_col = cell.x

        if new_row < self.height:
            return self.cells[new_row][new_col]
        else:
            return None

    def get_right_neighbor(self, cell: Cell) -> Cell | None:

        new_row = cell.y
        new_col = cell.x + 1

        if new_col < self.width:
            return self.cells[new_row][new_col]
        else:
            return None

    def get_left_neighbor(self, cell: Cell) -> Cell | None:

        new_row = cell.y
        new_col = cell.x - 1

        if new_col >= 0:
            return self.cells[new_row][new_col]
        else:
            return None

    def get_orth_neighbors(self, cell: Cell) -> dict[str, Cell]:
        neighbors = {}

        left = self.get_left_neighbor(cell)
        right = self.get_right_neighbor(cell)
        up = self.get_up_neighbor(cell)
        down = self.get_down_neighbor(cell)

        if left is not None:
            neighbors["left"] = left
        if right is not None:
            neighbors["right"] = right
        if up is not None:
            neighbors["up"] = up
        if down is not None:
            neighbors["down"] = down

        return neighbors

    def get_cells_to_check(self) -> list[Cell]:
        cells_to_check: list[Cell] = []

        for row in self.cells:
            for cell in row:
                cells_to_check.append(cell)

        heapq.heapify(cells_to_check)

        return cells_to_check

    # def get_heap(self) -> list[Cell]:
    #     heap: list[Cell] = []

    #     for row in self.cells:
    #         for cell in row:
    #             heap.append(cell)

    #     heapq.heapify(heap)

    #     return heap

    def reweigh_neighbor(self, start_cell: Cell, neighbor_cell: Cell):
        new_wt = start_cell.weight + int(neighbor_cell.value)

        if new_wt < neighbor_cell.weight:
            neighbor_cell.weight = new_wt
            heapq.heappush(self.cells_to_check, neighbor_cell)

    def reweigh_neighbors(self, start_cell: Cell):
        neighbors = self.get_orth_neighbors(start_cell)

        for neighbor in neighbors:
            self.reweigh_neighbor(start_cell, neighbors[neighbor])

    def print_weights(self):
        for row in self.cells:
            row_str = ""
            for cell in row:
                row_str += str(cell.weight) + ", "
            print(row_str)

    def print_values(self):
        for row in self.cells:
            row_str = ""
            for cell in row:
                row_str += str(cell.value) + ", "
            print(row_str)

    def weigh_cells_dumb(self):
        for row in range(self.height):
            for col in range(self.width):
                self.reweigh_neighbors(self.cells[col][row])

        return self.cells[self.height - 1][self.width - 1].weight

    def reweigh_next_cells(self):
        cell_to_check = heapq.heappop(self.cells_to_check)
        self.reweigh_neighbors(cell_to_check)

    def get_wt_at(self, destination: Cell) -> int:
        while destination.weight > 999999999:
            self.reweigh_next_cells()

        return int(destination.weight)

    # def weigh_cells(self):
    #     while self.cells[self.height - 1][self.width - 1].weight > 9999999999999:
    #         cell_to_check = heapq.heappop(self.heap)
    #         self.reweigh_neighbors(cell_to_check)

    #         self.print_weights()
    #         print("---------")

    #     return self.cells[self.height - 1][self.width - 1].weight


def p1() -> str:

    grid = Grid(dataset)

    answer = f"{grid.get_wt_at(grid.cells[grid.height - 1][grid.width - 1])}"

    grid.print_weights()

    print(answer)

    return answer


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


# class Grid:
#     def __init__(self, input_lines: list[str]) -> None:
#         self.lines = input_lines
#         self.width = len(input_lines[0])
#         self.height = len(input_lines)
#         self.cells: list[list[int]] = []

#         for line in self.lines:
#             new_row = []
#             for c in line:
#                 new_row.append(int(c))
#             self.cells.append(new_row)

#     def print_lines(self):
#         for line in self.lines:
#             print(line)

#     def convert_to_cell_num(self, coords: tuple[int, int]) -> int:
#         x, y = coords
#         return y * self.width + x

#     def convert_to_coords(self, cell_num: int) -> tuple[int, int]:
#         x = cell_num % self.width
#         y = math.floor(cell_num / self.width)

#         return (x, y)
