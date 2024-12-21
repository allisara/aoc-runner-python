from shared import get_dataset
from os import getenv
from grid import Point, Grid

dataset = get_dataset()
p1_test_case_answer: str = "8"


class Pipe_Map(Grid):
    def __init__(self, input: list[str]) -> None:
        super().__init__(input)
        self.start_point = (0, 0)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                point = self.get_value_at_coord((x, y))
                if point == "S":
                    self.start_point = (x, y)
                    break

        self.connected_directions = {
            "S": ["up", "right", "down", "left"],
            "L": ["up", "right"],
            "|": ["up", "down"],
            "F": ["right", "down"],
            "-": ["right", "left"],
            "7": ["down", "left"],
            "J": ["up", "left"],
            ".": []}

    def get_step_count(self) -> int:
        step_count = 0

        current_step = self.start_point
        next_step = self.get_connections(current_step)[0]

        still_looking = True

        while still_looking:
            step_count += 1

            x, y = current_step
            self.grid[y][x].visited = True

            next_connections = self.get_connections(next_step)
            next_connections.remove(current_step)
            current_step = next_step
            next_step = next_connections[0]

            if current_step == self.start_point:
                still_looking = False

        return step_count

    def get_connections(self, coord: tuple[int, int]) -> list[tuple[int, int]]:
        connections = []
        current_val = self.get_value_at_coord(coord)

        for direction in self.connected_directions[current_val]:
            neighbor_coord = self.get_neighbor(coord, direction)
            if self.is_in_bounds(neighbor_coord):
                neighbor_val = self.get_value_at_coord(neighbor_coord)
                for way in self.connected_directions[neighbor_val]:
                    if self.get_neighbor(neighbor_coord, way) == coord:
                        connections.append(neighbor_coord)

        return connections


def p1() -> str:
    # Solve code here, return string to submit

    pipes = Pipe_Map(dataset)

    print(pipes)

    answer = int(pipes.get_step_count() / 2)

    print(answer)

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
