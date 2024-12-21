from __future__ import annotations
from shared import get_dataset
from os import getenv
from typing import TypeVar, Generic
import heapq
import math

T = TypeVar("T")

dataset = get_dataset()
p1_test_case_answer: str = "7036"


class Cell(Generic[T]):
    def __init__(self, x: int, y: int, value: T, direction: str) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.weight = math.inf
        self.direction = direction
        self.visited = False

        # self.neighboring_coords = [(x-1, y-1), (x, y-1), (x + 1, y - 1),
        #                   (x-1, y), (x + 1, y),
        #                   (x-1, y+1), (x, y+1), (x + 1, y + 1)]

    def __lt__(self, other: Cell) -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"{self.value} ({self.x}, {self.y})"


class Grid:
    def __init__(self, input: list[str], direction: str) -> None:
        self.input = input
        self.height = len(input)
        self.width = len(input[0])
        self.direction = direction

        self.cells = self.create_cells()
        self.start: Cell
        self.end: Cell

        # self.cells[0][0].weight = 0
        # self.cells_to_check = [self.cells[0][0]]
        # heapq.heapify(self.cells_to_check)

    def create_cells(self) -> list[list[Cell]]:

        grid_input = []

        for row in range(len(self.input)):
            row_cells = []
            for col in range(len(self.input[0])):
                new_cell = Cell(col, row, self.input[row][col], self.direction)
                row_cells.append(new_cell)
                if new_cell.value == "S":
                    self.start = new_cell
                if new_cell.value == "E":
                    self.end = new_cell
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

    def get_neighbor(self, cell: Cell, direction: str) -> Cell | None:
        if direction == "right":
            return self.get_right_neighbor(cell)
        elif direction == "down":
            return self.get_down_neighbor(cell)
        elif direction == "left":
            return self.get_left_neighbor(cell)
        elif direction == "up":
            return self.get_up_neighbor(cell)
        error = Cell(0, 0, "!", "right")
        error.weight = math.inf
        return error

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


grids = {"right": Grid(dataset, "right"), "down": Grid(
    dataset, "down"), "left": Grid(dataset, "left"), "up": Grid(dataset, "up")}

grids["right"].start.weight = 0

cells_to_check = []


def reweigh_neighbors(current: Cell):
    next_cell = grids[current.direction].get_neighbor(
        current, current.direction)
    if next_cell != None:
        if next_cell.value != "#":
            if not next_cell.visited:
                next_cell.visited = True
                if next_cell.weight > current.weight + 1:
                    next_cell.weight = current.weight + 1
                    print(f"pushing {next_cell.weight} at {next_cell.x}, {
                        next_cell.y} going {next_cell.direction}")
                    heapq.heappush(cells_to_check, next_cell)

    if current.direction == "up" or current.direction == "down":
        turn_1 = grids["left"].cells[current.y][current.x]
        turn_2 = grids["right"].cells[current.y][current.x]

        if turn_1.weight > current.weight + 1000:
            turn_1.weight = current.weight + 1000
            print(f"pushing {turn_1.weight} at {turn_1.x}, {
                  turn_1.y} going {turn_1.direction}")
            heapq.heappush(cells_to_check, turn_1)

        if turn_2.weight > current.weight + 1000:
            turn_2.weight = current.weight + 1000
            print(f"pushing {turn_2.weight} at ({turn_2.x}, {
                turn_2.y}) going {turn_2.direction}")
            heapq.heappush(cells_to_check, turn_2)

    else:
        turn_1 = grids["up"].cells[current.y][current.x]
        turn_2 = grids["down"].cells[current.y][current.x]

    if turn_1.weight > current.weight + 1000:
        turn_1.weight = current.weight + 1000
        print(f"pushing {turn_1.weight} at {turn_1.x}, {
              turn_1.y} going {turn_1.direction}")
        heapq.heappush(cells_to_check, turn_1)

    if turn_2.weight > current.weight + 1000:
        turn_2.weight = current.weight + 1000
        print(f"pushing {turn_2.weight} at ({turn_2.x}, {
            turn_2.y}) going {turn_2.direction}")
        heapq.heappush(cells_to_check, turn_2)

    return


def step():
    next_step = heapq.heappop(cells_to_check)
    reweigh_neighbors(next_step)


def get_min_wt(c: Cell) -> float:
    min_wt = float(c.weight)
    row = c.y
    col = c.x
    if grids["right"].cells[row][col].weight < min_wt:
        min_wt = grids["right"].cells[row][col].weight
    if grids["down"].cells[row][col].weight < min_wt:
        min_wt = grids["down"].cells[row][col].weight < min_wt
    if grids["left"].cells[row][col].weight < min_wt:
        min_wt = grids["left"].cells[row][col].weight < min_wt
    if grids["up"].cells[row][col].weight < min_wt:
        min_wt = grids["up"].cells[row][col].weight < min_wt
    return min_wt


def debug_grids():
    for row in grids["right"].cells:
        new_row = ""
        for c in row:
            if c.weight > 9999999:
                new_row = new_row + c.value
            else:
                w = int(math.floor(c.weight / 1000))
                new_row = new_row + str(w)
        print(new_row)


def p1() -> str:

    for grid in grids.keys():
        for row in grids[grid].cells:
            for cell in row:
                cells_to_check.append(cell)

    heapq.heapify(cells_to_check)

    # while get_min_wt(grids["right"].end) > 999999999999999:
    #     step()

    for i in range(20):
        step()
        debug_grids()

    # print(get_min_wt(grids["right"].cells[12][1]))

    return f"{get_min_wt(grids["right"].end)}"


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
