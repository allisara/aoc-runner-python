from shared import get_dataset
from os import getenv
from grid import Grid, Point

dataset = get_dataset()
p1_test_case_answer: str = "16"

garden_map = Grid(dataset)


def p1() -> str:
    # Solve code here, return string to submit

    start_pt = Point("test", 0, 0)

    test_pt = Point("test", 0, 0)

    for position in garden_map.grid:
        if garden_map.grid[position].value == "S":
            start_pt = garden_map.grid[position]
            break

    next_steps = [start_pt]

    for i in range(64):
        next_steps = get_next_steps(next_steps, garden_map)
        next_steps = remove_duplicates(next_steps)
        print_points(next_steps)

    print_current_steps(next_steps, garden_map)

    answer = len(next_steps)

    return f"{answer}"


def get_next_steps(current_steps: list[Point], map: Grid) -> list[Point]:
    next_steps: list[Point] = []

    for step in current_steps:
        adjacents = map.get_adjacents(step)
        for potential_step in adjacents:
            if potential_step.value != "#" and potential_step not in next_steps:
                next_steps.append(potential_step)

    return next_steps


def print_current_steps(current_steps: list[Point], map: Grid):
    current_map = map.get_copy()
    for step in current_steps:
        current_map.grid[step.get_coords()].value = "O"

    print(current_map)


def print_points(points: list[Point]):
    string = ""

    for point in points:
        string += f"[{point.get_coords()}] "

    print(string)


def remove_duplicates(points: list[Point]) -> list[Point]:
    new_list: list[Point] = []
    coords: list[tuple[int, int]] = []
    for point in points:
        coord = point.get_coords()
        if coord not in coords:
            coords.append(coord)
            new_list.append(point)
    return new_list


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
