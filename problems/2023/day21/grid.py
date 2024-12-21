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
        self.width = len(input[0])
        self.height = len(input)

    def __str__(self) -> str:
        string = "\n"

        for row in range(self.height):
            next_row = ""
            for col in range(self.width):
                next_row += self.grid[(col, row)].value + " "
            string += next_row + "\n"

        return string

    def build_grid(self, input: list[str]) -> dict[tuple[int, int], Point]:
        grid: dict[tuple[int, int], Point] = {}
        for row in range(len(input)):
            for col in range(len(input[row])):
                next_pt = Point(input[row][col], col, row)
                grid[(col, row)] = next_pt
        return grid

    def get_adjacents(self, start: Point, include_diagonals=False) -> list[Point]:
        adjacents: list[Point] = []

        dir_to_check = ["up", "down", "left", "right"]
        if include_diagonals:
            dir_to_check += ["ne", "nw", "se", "sw"]

        for direction in dir_to_check:
            x, y = self.get_neighbor_coord(start, direction)
            new_point = Point("", x, y)

            if self.is_in_bounds(new_point):
                new_point.value = self.grid[(new_point.x, new_point.y)].value
                adjacents.append(new_point)

        return adjacents

    def get_neighbor(self, start: Point, direction: str) -> Point:
        return (self.grid[self.get_neighbor_coord(start, direction)])

    def get_neighbor_coord(self, start: Point, direction: str) -> tuple[int, int]:
        if direction == "right":
            return (start.x+1, start.y)
        elif direction == "left":
            return (start.x-1, start.y)
        elif direction == "up":
            return (start.x, start.y-1)
        elif direction == "down":
            return (start.x, start.y+1)
        elif direction == "nw":
            return (start.x-1, start.y-1)
        elif direction == "ne":
            return (start.x+1, start.y-1)
        elif direction == "sw":
            return (start.x-1, start.y+1)
        elif direction == "se":
            return (start.x+1, start.y+1)

        return (-999, -999)

    def is_in_bounds(self, point: Point) -> bool:
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def get_copy(self):
        copy = Grid(["t"])
        copy.grid = self.grid
        copy.height = self.height
        copy.width = self.width

        return copy

    # def is_in_bounds(self, coord: tuple[int, int]) -> bool:
    #     max_y = len(self.grid) - 1
    #     max_x = len(self.grid[0]) - 1

    #     x, y = coord

    #     return 0 <= x <= max_x and 0 <= y <= max_y

    # def get_neighbor_coords(self, coord: tuple[int, int], direction: str) -> tuple[int, int]:
    #     x, y = coord
    #     delta_x, delta_y = self.get_new_coord((x, y), direction)
    #     return (x + delta_x, y + delta_y)

    # def get_neighbor(self, start: Point, direction: str) -> Point:
    #     delta_x, delta_y = self.get_new_coord((start.x, start.y), direction)
    #     return self.grid[start.y + delta_y][start.x + delta_x]

    # def get_adjacent_coords(self, coord: tuple[int, int], include_diagonals=False) -> list[tuple[int, int]]:
    #     adjacents = []

    #     dir_to_check = ["up", "down", "left", "right"]
    #     if include_diagonals:
    #         dir_to_check += ["ne", "nw", "se", "sw"]

    #     for direction in dir_to_check:
    #         new_coord = self.get_neighbor_coords(coord, direction)
    #         if self.is_in_bounds(new_coord):
    #             adjacents.append(new_coord)

    #     return adjacents

    # def get_row_values(self, row_num: int) -> list[str]:
    #     row = []

    #     for thing in self.grid[row_num]:
    #         row.append(thing.value)

    #     return row

    # def get_col_values(self, col_num: int) -> list[str]:
    #     col = []

    #     for i in range(len(self.grid)):
    #         col.append(self.grid[i][col_num].value)

    #     return col

    # def get_manhattan_distance(self, a: tuple[int, int], b: tuple[int, int]) -> int:
    #     a_x, a_y = a
    #     b_x, b_y = b

    #     x_delta = abs(a_x - b_x)
    #     y_delta = abs(a_y - b_y)

    #     return x_delta + y_delta

    # def get_value_at_coord(self, x: int, y: int) -> str:
    #     return self.grid[y][x].value
