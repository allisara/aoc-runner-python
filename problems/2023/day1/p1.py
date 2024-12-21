from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "142"


def p1() -> str:
    # Solve code here, return string to submit
    answer = 0

    for line in dataset:
        answer += get_cal_val(line)

    return f"{answer}"


def get_first_int(s) -> str:
    first_int = ""
    for char in s:
        if first_int == "":
            char_value = ord(char)
            if char_value >= 48 and char_value <= 57:
                first_int = char

    return first_int


def get_last_int(s) -> str:
    last_int = ""
    for char in s:
        char_value = ord(char)
        if char_value >= 48 and char_value <= 57:
            last_int = char

    return last_int


def get_cal_val(s) -> int:
    return int(get_first_int(s) + get_last_int(s))


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")

    print(get_cal_val("a234r7t"))

    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
