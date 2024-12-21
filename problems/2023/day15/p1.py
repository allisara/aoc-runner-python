from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "1320"


def convert_string(string: str) -> int:
    current_value = 0

    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


def p1() -> str:
    # Solve code here, return string to submit

    answer = 0

    for command in dataset:
        answer += convert_string(command)
        # print(f"{command} becomes {convert_string(command)}")

    # print(dataset)

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
