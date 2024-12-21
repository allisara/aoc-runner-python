from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "62"

trench = []
border = []

go = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def p1() -> str:
    # Solve code here, return string to submit

    y_max: int = 0
    y_min: int = 0
    x_max: int = 0
    x_min: int = 0

    for line in dataset:
        if len(trench) > 0:
            start_pt = trench[-1]
        else:
            start_pt = (0, 0)
        direction = go[line[0]]
        length = int(line[1])
        x, y = start_pt
        delta_x, delta_y = direction

        for i in range(1, length + 1):
            new_x = x + delta_x * i
            new_y = y + delta_y * i
            x_max = max(new_x, x_max)
            x_min = min(new_x, x_min)
            y_max = max(y_max, new_y)
            y_min = min(y_min, new_y)

            trench.append((new_x, new_y))

    for i in range(x_min - 2, x_max + 2, 1):
        border.append((i, y_min - 2))
        border.append((i, y_max + 2))

    for i in range(y_min - 2, y_max + 2, 1):
        border.append((x_min - 2, i))
        border.append((x_max + 2, i))

    outside_squares = []
    squares_to_check = [(x_min - 1, y_min - 1)]

    while len(squares_to_check) > 0:
        next_sq = squares_to_check[0]
        squares_to_check.remove(next_sq)

        if next_sq not in border and next_sq not in outside_squares:
            outside_squares.append(next_sq)
            col, row = next_sq
            squares_to_check.append((col + 1, row))
            squares_to_check.append((col - 1, row))
            squares_to_check.append((col, row + 1))
            squares_to_check.append((col, row - 1))

    # answer = ((x_max + 1) - (x_min - 1)) * \
    #     (y_max - y_min + 2) - len(outside_squares)

    # print(f"X: {x_min} - {x_max}")
    # print(f"Y: {y_min} - {y_max}")

    # print(answer)

    answer = len(outside_squares)

    outside_squares = []
    squares_to_check = [(x_min - 1, y_min - 1)]

    while len(squares_to_check) > 0:
        next_sq = squares_to_check[0]
        squares_to_check.remove(next_sq)

        if next_sq not in border and next_sq not in outside_squares and next_sq not in trench:
            outside_squares.append(next_sq)
            col, row = next_sq
            squares_to_check.append((col + 1, row))
            squares_to_check.append((col - 1, row))
            squares_to_check.append((col, row + 1))
            squares_to_check.append((col, row - 1))

    answer -= len(outside_squares)

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
