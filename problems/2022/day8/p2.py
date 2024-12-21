from shared import get_dataset, Plant
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "8"


def is_on_edge(row: int, col: int) -> bool:
    if row is 0 or row is len(dataset) - 1:
        return True
    elif col is 0 or col is len(dataset[0]) - 1:
        return True
    else:
        return False


def p2() -> str:
    # Solve code here, return string to submit
    for row_num, row in enumerate(dataset):
        for col_num, plant in enumerate(row):
            up_trees: int = 0
            down_trees: int = 0
            left_trees: int = 0
            right_trees: int = 0
            if is_on_edge(row_num, col_num):
                break
            else:
                return

    return ""


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
