from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "4"


def is_overlapped(a_min, a_max, b_min, b_max):
    if a_min >= b_min and a_min <= b_max:
        return True

    elif a_max >= b_min and a_max <= b_max:
        return True

    elif b_max >= a_min and b_max <= a_max:
        return True

    elif b_min >= a_min and b_min <= a_max:
        return True

    return False


def p2() -> str:
    # Solve code here, return string to submit

    # Turn dataset into a 1 level list of ints called ranges

    inputs_list = []
    ranges = []
    answer = 0

    for pair in dataset:
        split_pair = pair.split(",")
        range_pair = split_pair[0] + "-" + split_pair[1]
        range_pair = range_pair.split("-")

        inputs_list.append(range_pair)

    for pair in inputs_list:
        for values in pair:
            ranges.append(int(values))

    # count the number of pairs where one list fully contains the other
    for i in range(0, len(ranges), 4):
        if is_overlapped(ranges[i], ranges[i+1], ranges[i+2], ranges[i+3]):
            answer += 1

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {'nothing' if p2_answer=='' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
