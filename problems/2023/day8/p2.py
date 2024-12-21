from shared import get_dataset
from os import getenv

import math

dataset = get_dataset()
p2_test_case_answer: str = "6"

dir_str = dataset.pop(0)

DIRECTIONS = []
for c in dir_str:
    if c == "L":
        DIRECTIONS.append(0)
    elif c == "R":
        DIRECTIONS.append(1)
    else:
        print("Invalid direction")
DIR_NUM = len(DIRECTIONS)

MAP = {}
for map_line in dataset:
    line = map_line.split(" = (")
    node = line[0]
    l_r = line[1].replace(")", "").split(", ")
    MAP[node] = (l_r[0], l_r[1])

ends_in_A = []
ends_in_Z = []


def get_next_node(current_node: str, direction: int) -> str:
    next_nodes = MAP[current_node]
    return next_nodes[direction]


def ends_with(letter: str, node: str) -> bool:
    return node[-1] == letter


def all_end_with(letter: str, nodes: list[str]) -> bool:
    for node in nodes:
        if not ends_with(letter, node):
            return False
    return True


def check_path(start_node: str) -> None:
    still_looking = True
    step_count = 0

    current_node = start_node

    print(f"For starting node {start_node}:")

    while still_looking:
        next_dir = DIRECTIONS[step_count % DIR_NUM]
        step_count += 1
        next_node = get_next_node(current_node, next_dir)
        # if ends_with("Z", next_node):
        #     print(f"Z found at step {step_count}")
        # elif start_node == next_node:
        #     still_looking = False
        #     print(f"Returns to start in {step_count} steps")
        # elif step_count > 8000:
        #     print("Doesn't return to start")
        #     still_looking = False
        print(next_node)
        if step_count > 10:
            still_looking = False
        current_node = next_node

    return


def get_loop_length(start_node: str) -> int:
    still_looking = True
    step_count = 0

    first_z = ""
    found_z = False
    loop_length = 0

    current_node = start_node

    print(f"For starting node {start_node}:")

    while still_looking:
        next_dir = DIRECTIONS[step_count % DIR_NUM]
        step_count += 1
        next_node = get_next_node(current_node, next_dir)

        if found_z:
            loop_length += 1

        # print(next_node)

        if next_node in ends_in_Z:
            if found_z and next_node == first_z:
                print(
                    f"Found {next_node} again. Loop size is {loop_length} and total steps are {step_count}")
                # loop_length = 0
                still_looking = False
                return loop_length
            elif not found_z:
                first_z = next_node
                found_z = True
                print(f"Z found in {next_node} at step {step_count}")
        elif next_node == start_node:
            still_looking = False
            print(f"Returns to start in {step_count} steps")
        if step_count > 100000:
            print("Doesn't return to start")
            still_looking = False
        current_node = next_node

    return -1


def p2() -> str:
    step_count = 0
    loop_lengths = []

    for node in MAP:
        if ends_with("A", node):
            ends_in_A.append(node)
        if ends_with("Z", node):
            ends_in_Z.append(node)

    print(ends_in_A)

    for node in ends_in_A:
        loop_lengths.append(get_loop_length(node))
        print("")

    print(loop_lengths)

    answer = math.lcm(loop_lengths[0], loop_lengths[1], loop_lengths[2],
                      loop_lengths[3], loop_lengths[4], loop_lengths[5])

    answer2 = math.lcm(*loop_lengths)
    print(answer2)

    # for node in nodes_to_check:
    #     check_path(node)

    # while still_looking:
    #     next_dir = DIRECTIONS[step_count % dir_num]
    #     step_count += 1

    #     next_nodes_to_check = []
    #     for node in nodes_to_check:
    #         next_nodes_to_check.append(get_next_node(node, next_dir))
    #     if all_end_with("Z", next_nodes_to_check):
    #         still_looking = False
    #     nodes_to_check = next_nodes_to_check

    # -----------------------------------------------------

    # current_node = "AAA"

    # while still_looking:
    #     next_dir = DIRECTIONS[step_count % dir_num]
    #     step_count += 1
    #     next_node = get_next_node(current_node, next_dir)
    #     if next_node == "ZZZ":
    #         still_looking = False
    #     current_node = next_node

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
