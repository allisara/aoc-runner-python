from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "281"

all_digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0, "one": 1,
              "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def p2() -> str:
    # Solve code here, return string to submit

    answer = 0

    for line in dataset:
        answer += find_first_digit(line)*10 + find_last_digit(line)

    # print(find_last_digit("afourtwobc123foursdgsh"))

    return f"{answer}"


def find_first_digit(s) -> int:
    first_digit_pos = 99999999
    first_digit = 9999999
    for digit in all_digits:
        pos = s.find(digit)
        if -1 < pos < first_digit_pos:
            first_digit_pos = pos
            first_digit = all_digits[digit]

    return first_digit


def find_last_digit(s) -> int:
    last_digit = -99999999
    last_digit_pos = -9999999
    for digit in all_digits:
        pos = s.find(digit)
        if pos > last_digit_pos:
            last_digit_pos = pos
            last_digit = all_digits[digit]

    tail = s[last_digit_pos + 1:]
    keep_going = False

    for digit in all_digits:
        if tail.find(digit) >= 0:
            keep_going = True

    if keep_going:
        last_digit = find_last_digit(tail)

    return last_digit


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
