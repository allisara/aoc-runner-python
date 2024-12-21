from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def find_marker(input: str, marker_length: int):
    marker = -99

    for i in range(len(input)):
        check_string = input[i: i + marker_length]
        if len(check_string) == len(set(check_string)):
            return i + marker_length

    return marker


def p2() -> str:
    # Solve code here, return string to submit
    return f"{find_marker(dataset[0], 14)}"


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
