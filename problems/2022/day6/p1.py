from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "7"


def find_marker(input, marker_length):
    marker = -99

    for i in range(len(input)):
        check_string = input[i: i + marker_length]
        print(i)
        print(check_string)
        if len(check_string) == len(set(check_string)):
            return i + marker_length

    return marker


def p1() -> str:
    # Solve code here, return string to submit
    # print(dataset)

    return f"{find_marker(dataset[0], 4)}"


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
