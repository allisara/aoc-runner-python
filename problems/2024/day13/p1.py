from __future__ import annotations
from shared import get_dataset
from os import getenv


dataset = get_dataset()
p1_test_case_answer: str = "480"


def get_tokens(Ax: int, Ay: int, Bx: int, By: int, X: int, Y: int) -> int:

    Anum = (Bx * Y - By*X)/(Bx * Ay - By * Ax)
    Bnum = (X - Ax * Anum) / Bx

    if Anum.is_integer() and Bnum.is_integer():
        print(f"Anum: {Anum}, Bnum: {Bnum}")
        return int(3 * Anum + Bnum)

    return 0


def p1() -> str:
    # Solve code here, return string to submit
    answer = 0

    for i in range(0, len(dataset), 6):
        machine = dataset[i:i+6]
        print(machine)
        answer += get_tokens(*machine)

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
