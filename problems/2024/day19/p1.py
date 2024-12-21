from __future__ import annotations
from shared import get_dataset
from os import getenv
from functools import lru_cache

dataset = get_dataset()
p1_test_case_answer: str = "6"

patterns = dataset[0].split(", ")
patterns.sort(key=len, reverse=True)
designs = dataset[1:]


@lru_cache
def is_possible(design: str) -> bool:
    global patterns
    for pattern in patterns:
        if pattern == design:
            return True
        if len(design) > len(pattern) and design[:len(pattern)] == pattern:
            if is_possible(design[len(pattern):]):
                return True
    return False


def p1() -> str:

    answer = 0

    for design in designs:
        if is_possible(design):
            print(f"{design} is possible")
            answer += 1
        else:
            print(f"{design} is not possible")

    print(answer)

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
