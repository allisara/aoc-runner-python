from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p2() -> str:
    # Solve code here, return string to submit

    x: int = 1

    x_values: list[int] = []

    for command in dataset:

        if command.startswith("noop"):
            x_values.append(x)

        else:
            x_values.append(x)
            x_values.append(x)
            x += int(command.split()[1])

    row_1: str = ""
    row_2: str = ""
    row_3: str = ""
    row_4: str = ""
    row_5: str = ""
    row_6: str = ""

    for clock in range(40):
        if x_values[clock] - 1 <= clock <= x_values[clock] + 1:
            row_1 += "#"
        else:
            row_1 += "."

    for clock in range(40, 80, 1):
        if x_values[clock] - 1 <= clock - 40 <= x_values[clock] + 1:
            row_2 += "#"
        else:
            row_2 += "."

    for clock in range(80, 120, 1):
        if x_values[clock] - 1 <= clock - 80 <= x_values[clock] + 1:
            row_3 += "#"
        else:
            row_3 += "."

    for clock in range(120, 160, 1):
        if x_values[clock] - 1 <= clock - 120 <= x_values[clock] + 1:
            row_4 += "#"
        else:
            row_4 += "."

    for clock in range(160, 200, 1):
        if x_values[clock] - 1 <= clock - 160 <= x_values[clock] + 1:
            row_5 += "#"
        else:
            row_5 += "."

    for clock in range(200, 240, 1):
        if x_values[clock] - 1 <= clock - 200 <= x_values[clock] + 1:
            row_6 += "#"
        else:
            row_6 += "."

    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
    print(row_6)
    # print(x_values)

    return "PAPJCBHP"


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
