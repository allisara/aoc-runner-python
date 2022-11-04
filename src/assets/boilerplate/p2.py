from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p2() -> str:
    # Solve code here, return string to submit
    return ""


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_SHORT"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {'nothing' if p2_answer=='' else p2_answer}\nshould be {p2_test_case_answer}\n\n"
    print(f"\n\nfunction p2 returned {p2_answer}\nAnswer is CORRECT\n\n")
elif __name__ == '__main__':
    print(p2())
