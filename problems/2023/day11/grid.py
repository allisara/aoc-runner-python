class Point():
    def __init__(self, val: str, x: int, y: int) -> None:
        self.value = val
        self.x = x
        self.y = y
        self.visited = False

    def __str__(self) -> str:
        return f"{self.value} at ({self.x}, {self.y})"

    def get_coords(self) -> tuple[int, int]:
        return (self.x, self.y)


class Grid():
    def __init__(self, input: list[str]) -> None:
        self.grid = self.build_grid(input)

    def __str__(self) -> str:
        string = "\n"

        for row in self.grid:
            for point in row:
                string += point.value + " "
            string += "\n"

        return string

    def build_grid(self, input: list[str]) -> list[list[Point]]:
        grid = []

        for row in range(len(input)):
            next_row = []
            for col in range(len(input[row])):
                next_pt = Point(input[row][col], col, row)
                next_row.append(next_pt)
            grid.append(next_row)

        return grid

    def get_value_at_coord(self, x: int, y: int) -> str:
        return self.grid[y][x].value

    def get_new_coord(self, coord: tuple[int, int], direction: str) -> tuple[int, int]:
        x, y = coord
        if direction == "right":
            return (x+1, y)
        elif direction == "left":
            return (x-1, y)
        elif direction == "up":
            return (x, y-1)
        elif direction == "down":
            return (x, y+1)
        elif direction == "nw":
            return (x-1, y-1)
        elif direction == "ne":
            return (x+1, y-1)
        elif direction == "sw":
            return (x-1, y+1)
        elif direction == "se":
            return (x+1, y+1)

        return (-999, -999)

    def is_in_bounds(self, coord: tuple[int, int]) -> bool:
        max_y = len(self.grid) - 1
        max_x = len(self.grid[0]) - 1

        x, y = coord

        return 0 <= x <= max_x and 0 <= y <= max_y

    def get_neighbor(self, coord: tuple[int, int], direction: str) -> tuple[int, int]:
        x, y = coord
        delta_x, delta_y = self.get_new_coord((x, y), direction)
        return (x + delta_x, y + delta_y)

    def get_adjacent_coords(self, coord: tuple[int, int], include_diagonals=False) -> list[tuple[int, int]]:
        adjacents = []

        dir_to_check = ["up", "down", "left", "right"]
        if include_diagonals:
            dir_to_check += ["ne", "nw", "se", "sw"]

        for direction in dir_to_check:
            new_coord = self.get_neighbor(coord, direction)
            if self.is_in_bounds(new_coord):
                adjacents.append(new_coord)

        return adjacents

    def get_row(self, row_num: int) -> list[str]:
        row = []

        for thing in self.grid[row_num]:
            row.append(thing.value)

        return row

    def get_col(self, col_num: int) -> list[str]:
        col = []

        for i in range(len(self.grid)):
            col.append(self.grid[i][col_num].value)

        return col

    def get_manhattan_distance(self, a: tuple[int, int], b: tuple[int, int]) -> int:
        a_x, a_y = a
        b_x, b_y = b

        x_delta = abs(a_x - b_x)
        y_delta = abs(a_y - b_y)

        return x_delta + y_delta
