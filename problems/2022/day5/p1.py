from shared import get_dataset, get_tops
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "CMZ"


def move_box(all_boxes, start_pos, end_pos):
    #box = all_boxes
    # print(all_boxes[start_pos][-1])
    all_boxes[end_pos] += all_boxes[start_pos][-1]
    all_boxes[start_pos].pop()
    # print(all_boxes)

    return all_boxes


def move_boxes(all_boxes, commands):
    num_of_boxes, start_pos, end_pos = commands

    for i in range(num_of_boxes):
        all_boxes = move_box(all_boxes, start_pos - 1, end_pos - 1)

    return all_boxes


def p1() -> str:
    # Solve code here, return string to submit

    crates, instructions = get_dataset()

    print(crates)
    print(instructions)

    for command in instructions:
        crates = move_boxes(crates, command)

    print(crates)

    return f"{get_tops(crates)}"


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
