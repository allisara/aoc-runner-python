from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p1() -> str:
    # Solve code here, return string to submit
    return ""


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_SHORT"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}\n\n"
    print(f"\n\nfunction p1 returned {p1_answer}\nAnswer is CORRECT\n\n")
elif __name__ == '__main__':
    print(p1())
