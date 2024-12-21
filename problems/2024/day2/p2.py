from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "4"


def is_valid_pair(num1: int, num2: int, direction: int) -> bool:
    if num1 == num2:
        return False

    diff = (num2 - num1) * direction
    return 1 <= diff <= 3


def get_pair_direction(num1: int, num2: int) -> int:
    try:
        direction = int((num2 - num1) / abs(num2 - num1))
        # +1 = increasing; -1 = decreasing
    except ZeroDivisionError:
        direction = 0
    return direction


def get_direction(report: list[int]) -> int:
    num1: int = report[0]
    num2: int = report[1]
    num3: int = report[2]
    num4: int = report[3]

    overall_dir = get_pair_direction(
        num1, num2) + get_pair_direction(num2, num3) + get_pair_direction(num3, num4)

    if overall_dir > 0:
        return 1

    return -1


def is_error_free(report: list[int]) -> bool:
    direction = get_direction(report)

    for i in range(len(report) - 1):
        if not is_valid_pair(report[i], report[i+1], direction):
            return False

    return True


def get_variations(report: list[int]) -> list[list[int]]:
    variations = []

    for i in range(len(report)):
        new_list = report[:i] + report[i+1:]
        variations.append(new_list)

    return variations


def includes_safe_report(variations: list[list[int]]) -> bool:
    for list in variations:
        if is_error_free(list):
            return True
    return False


def is_safe(report: list[int]) -> bool:
    if is_error_free(report):
        return True

    variations = get_variations(report)

    if includes_safe_report(variations):
        return True
    return False


def p2() -> str:
    answer = 0

    for report in dataset:

        if is_safe(report):
            answer += 1

    return f"{answer}"


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
