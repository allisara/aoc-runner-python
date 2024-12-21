from __future__ import annotations
from shared import get_dataset
from os import getenv
from functools import lru_cache
from timeit import repeat

dataset = get_dataset()
p2_test_case_answer: str = "55312"


# setup_code = "from __main__ import blink"
# stmt = "blink(stones)"
# times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
# print(f"Minimum execution time: {min(times)}")


@lru_cache(maxsize=None)
def blink_stone(stone: str) -> list[str]:

    length = len(stone)

    if stone == "0":
        return ["1"]

    if length % 2 == 0:
        midpoint = length // 2
        new_left = stone[:midpoint]
        new_right = str(int(stone[midpoint:]))
        return [new_left, new_right]

    return [str(int(stone) * 2024)]


@lru_cache(maxsize=None)
def blink(stone: str, blink_num: int) -> int:
    if blink_num == 0:
        return 1

    child_stones = blink_stone(stone)

    answer = 0

    for child in child_stones:
        answer += blink(child, blink_num - 1)

    return answer


def p2() -> str:
    # Solve code here, return string to submit
    stones = dataset[0].split(" ")
    number_of_blinks = 75

    answer = 0

    for stone in stones:
        answer += blink(stone, number_of_blinks)

    print(blink_stone.cache_info())
    print(blink.cache_info())

    return f"{answer}"

    return ""


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
