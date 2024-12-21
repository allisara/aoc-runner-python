from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "31"

left_list: list[int] = []
right_list: list[int] = []

for line in dataset:
    number_strs = line.split("   ")
    left_list.append(int(number_strs[0]))
    right_list.append(int(number_strs[1]))


number_counts = {}

for num in left_list:
    number_counts[num] = 0

for num in right_list:
    if num in number_counts.keys():
        number_counts[num] += 1


def p2() -> str:
    answer = 0

    for i in range(len(left_list)):
        number = left_list[i]
        num_count = number_counts[number]
        answer += number * num_count

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
