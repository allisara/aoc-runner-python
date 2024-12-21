from shared import get_dataset, count_visible, Plant
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "21"


def check_row_from_left(plants: list[Plant]):
    min_height = -1
    for item in plants:
        if item.height > min_height:
            item.visible = True
            min_height = item.height

    return


def check_row_from_right(plants: list[Plant]):
    min_height = -1
    # for item in range(len(plants)-1, -1, -1):
    for item in reversed(plants):
        if item.height > min_height:
            item.visible = True
            min_height = item.height

    return


def check_columns(plants: list[list[Plant]]):
    transposed_tuples = list(zip(*plants))
    transposed_plants = [list(sublist) for sublist in transposed_tuples]

    for row in transposed_plants:
        check_row_from_left(row)
        check_row_from_right(row)

    return


def p1() -> str:
    # Solve code here, return string to submit

    for row in dataset:
        check_row_from_left(row)
        check_row_from_right(row)

    check_columns(dataset)

    # print(dataset)
    answer = count_visible(dataset)

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
