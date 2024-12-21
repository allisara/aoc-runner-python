from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "13140"


def p1() -> str:
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

        #print(f"{len(x_values)}: {x}")

    cycle_20 = x_values[19]

    cycle_60 = x_values[59]

    cycle_100 = x_values[99]

    cycle_140 = x_values[139]

    cycle_180 = x_values[179]

    cycle_220 = x_values[219]

    print(f"{20 * cycle_20}   {60 * cycle_60}   {100 * cycle_100}  {140 * cycle_140}   {180 * cycle_180}  { cycle_220}")

    answer = 20 * cycle_20 + 60 * cycle_60 + 100 * cycle_100 + \
        140 * cycle_140 + 180 * cycle_180 + 220 * cycle_220

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
