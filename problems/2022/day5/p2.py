from shared import get_dataset, get_tops
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "MCD"


def move_boxes(all_boxes, commands):
    num_of_boxes, start_pos, end_pos = commands

    lifted_boxes = []

    for i in range(num_of_boxes):
        lifted_boxes += all_boxes[start_pos-1][-1]
        all_boxes[start_pos-1].pop()

    lifted_boxes.reverse()
    all_boxes[end_pos - 1] += lifted_boxes

    # print(lifted_boxes)
    # print(all_boxes)

    return all_boxes


def p2() -> str:
    # Solve code here, return string to submit

    crates, instructions = get_dataset()

    # print(crates)
    # print(instructions)

    for command in instructions:
        crates = move_boxes(crates, command)

    # print(crates)

    return f"{get_tops(crates)}"


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
