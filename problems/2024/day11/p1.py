from __future__ import annotations
from shared import get_dataset
from os import getenv
from functools import lru_cache

dataset = get_dataset()
p1_test_case_answer: str = "55312"


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


def blink(stones: list[str]) -> list[str]:
    new_list: list[str] = []

    for stone in stones:
        new_list = new_list + blink_stone(stone)

    return new_list


def p1() -> str:
    # Solve code here, return string to submit
    stones = dataset[0].split(" ")

    number_of_blinks = 25

    for i in range(number_of_blinks):
        stones = blink(stones)
        # print(stones)

    print(blink_stone.cache_info())

    return f"{len(stones)}"


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
