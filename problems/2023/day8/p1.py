from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "6"

dir_str = dataset.pop(0)

DIRECTIONS = []
for c in dir_str:
    if c == "L":
        DIRECTIONS.append(0)
    elif c == "R":
        DIRECTIONS.append(1)
    else:
        print("Invalid direction")

MAP = {}
for map_line in dataset:
    line = map_line.split(" = (")
    node = line[0]
    l_r = line[1].replace(")", "").split(", ")
    MAP[node] = (l_r[0], l_r[1])


def get_next_node(current_node: str, direction: int) -> str:
    next_nodes = MAP[current_node]
    return next_nodes[direction]


def p1() -> str:
    still_looking = True
    dir_num = len(DIRECTIONS)
    step_count = 0
    current_node = "AAA"

    while still_looking:
        next_dir = DIRECTIONS[step_count % dir_num]
        step_count += 1
        next_node = get_next_node(current_node, next_dir)
        if next_node == "ZZZ":
            still_looking = False
        current_node = next_node

    return f"{step_count}"


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
