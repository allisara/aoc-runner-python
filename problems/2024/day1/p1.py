from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "11"

list1: list[int] = []
list2: list[int] = []

for line in dataset:
    number_strs = line.split("   ")
    list1.append(int(number_strs[0]))
    list2.append(int(number_strs[1]))

list1.sort()
list2.sort()


def p1() -> str:

    answer = 0

    for i in range(len(list1)):
        left = list1[i]
        right = list2[i]
        difference = abs(left - right)
        answer += difference

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
