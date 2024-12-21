from __future__ import annotations
from shared import get_dataset
from os import getenv
from time import perf_counter


def move_last_file(d: list[int | str], gap_index: int) -> list[int | str]:
    # d[gap_index] = d[-1]
    # new_drive = d[:-1]
    # # print(new_drive)
    # return new_drive
    file_id = d.pop()
    d[gap_index] = file_id

    print_drive(d)

    return d


def print_drive(d: list[int | str]):
    s = ""
    for item in d:
        s = s + str(item)
    # print(s)


dataset = get_dataset()
input_str = dataset[0]
p1_test_case_answer: str = "1928"

test_input = "12345"

drive: list[int | str] = []
gaps: list[int] = []

for i in range(0, len(input_str), 2):
    id_num = i//2
    file_size = int(input_str[i])
    try:
        gap_size = int(input_str[i+1])
    except IndexError:
        pass
    for __ in range(file_size):
        drive.append(id_num)
    for __ in range(gap_size):
        drive.append(".")

for i in range(len(drive)):
    if drive[i] == ".":
        gaps.append(i)


def p1() -> str:
    # Solve code here, return string to submit
    global drive
    global gaps

    first_gap_index = 0

    for i in range(len(gaps)):
        if drive[-1] == ".":
            drive = drive[:-1]
        else:
            drive = move_last_file(drive, gaps[first_gap_index])
            first_gap_index += 1

    # print(drive)
    answer = 0

    for i, val in enumerate(drive):
        answer += i * int(val)

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
    tic = perf_counter()
    p1_answer = "\n" + p1()
    toc = perf_counter()
    print(p1_answer)
    print(f"Solution took {toc - tic} seconds")
