from __future__ import annotations
from shared import get_dataset
from os import getenv
from functools import lru_cache

dataset = get_dataset()
p2_test_case_answer: str = "16"

patterns = dataset[0].split(", ")
patterns.sort(key=len, reverse=True)
designs = dataset[1:]


@lru_cache
def get_option_count(design: str) -> int:
    global patterns
    option_count = 0
    for pattern in patterns:
        if pattern == design:
            option_count += 1
        if len(design) > len(pattern) and design[:len(pattern)] == pattern:
            option_count += get_option_count(design[len(pattern):])
    return option_count


def p2() -> str:
    answer = 0

    for design in designs:
        answer += get_option_count(design)

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
