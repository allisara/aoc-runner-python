from shared import get_dataset
from os import getenv
from p1 import dir_sizes, p1

dataset = get_dataset()
p2_test_case_answer: str = "24933642"

p1()


def p2() -> str:
    # Solve code here, return string to submit
    used_space = dir_sizes["/"]
    min_space_to_free = used_space - 40_000_000

    answer = 1_000_000_000

    for value in dir_sizes.values():
        if value >= min_space_to_free and value < answer:
            answer = value

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
