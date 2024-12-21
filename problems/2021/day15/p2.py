from __future__ import annotations
from shared import get_dataset
from os import getenv
from p1 import Grid

dataset = get_dataset()
p2_test_case_answer: str = "315"


def increase_char(c: str, inc: int) -> str:
    start = int(c)
    new_num = start + inc

    if new_num > 9:
        new_num = new_num - 9

    return str(new_num)


def expand_row(original: str, x_factor: int) -> str:
    expanded_row = ""

    for i in range(x_factor):
        for c in original:
            expanded_row += increase_char(c, i)

    return expanded_row


def increase_row(original: str, x_factor: int) -> str:
    increased_row = ""
    for c in original:
        increased_row += increase_char(c, x_factor)

    return increased_row


def expand_block_horizontal(original: list[str], x_factor: int) -> list[str]:
    expanded_rows = []

    for line in original:
        expanded_rows.append(expand_row(line, x_factor))

    return expanded_rows


def expand_block_vertical(original: list[str], x_factor: int) -> list[str]:
    expanded_block = []

    for i in range(x_factor):
        for row in original:
            new_row = increase_row(row, i)
            expanded_block.append(new_row)

    return expanded_block


def expand_block(original: list[str], x_factor: int) -> list[str]:
    expanded_rows = expand_block_horizontal(original, x_factor)
    expanded_block = expand_block_vertical(expanded_rows, x_factor)

    return expanded_block


def p2() -> str:
    # Solve code here, return string to submit

    expanded_dataset = expand_block(dataset, 5)

    big_grid = Grid(expanded_dataset)

    # big_grid.print_values()

    answer = f"{big_grid.get_wt_at(
        big_grid.cells[big_grid.height - 1][big_grid.width - 1])}"

    print(answer)

    return answer


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
