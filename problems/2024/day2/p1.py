from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
reports: list[list[int]] = dataset
p1_test_case_answer: str = "2"


def is_valid_pair(num1: int, num2: int, direction: int) -> bool:
    diff = (num2 - num1) * direction
    return 1 <= diff <= 3


def is_safe_report(report: list[int]) -> bool:
    try:
        direction = int((report[1] - report[0]) / abs(report[1] - report[0]))
        # +1 = increasing; -1 = decreasing
    except ZeroDivisionError:
        direction = 1

    for i in range(len(report) - 1):
        if not is_valid_pair(report[i], report[i+1], direction):
            return False

    return True


def p1() -> str:
    answer = 0

    for report in dataset:
        if is_safe_report(report):
            answer += 1

    return f"{answer}"


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
