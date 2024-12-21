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

    def get_value_at_coord(self, coord: tuple[int, int]) -> str:
        x, y = coord
        return self.grid[y][x].value

    def get_neighbor(self, coord: tuple[int, int], direction: str) -> tuple[int, int]:
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

    # def get_neighbor(self, coord: tuple[int, int], direction: str) -> tuple[int, int]:
    #     return self.get_new_coord(coord, direction)

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
