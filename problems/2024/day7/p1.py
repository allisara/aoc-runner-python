from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "3749"


def evaluate_equation(answer: int, current_value: int, values: list[int]) -> bool:
    if current_value == answer and len(values) == 0:
        return True
    elif len(values) == 0 or current_value > answer:
        return False

    next_value = values[0]
    next_values = values[1:]

    if evaluate_equation(answer, current_value + next_value, next_values):
        return True

    if evaluate_equation(answer, current_value * next_value, next_values):
        return True

    return False


def p1() -> str:
    # Solve code here, return string to submit

    # print(evaluate_equation(156, 15, [6]))
    answer = 0

    for line in dataset:
        split_line = line.split(": ")

        all_values = split_line[1].split()
        first_value = int(all_values[0])
        strings_to_check = all_values[1:]
        values_to_check: list[int] = []

        for s in strings_to_check:
            values_to_check.append(int(s))

        target = int(split_line[0])

        if evaluate_equation(target, first_value, values_to_check):
            answer += target

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
