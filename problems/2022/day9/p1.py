from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "13"

head_pos: tuple[int, int] = (0, 0)
tail_pos: tuple[int, int] = (0, 0)
tail_spaces = {(0, 0)}


def get_up_pos(current_pos: tuple):
    new_pos = (current_pos[0], current_pos[1] + 1)
    return new_pos


def get_down_pos(current_pos: tuple):
    new_pos = (current_pos[0], current_pos[1] - 1)
    return new_pos


def get_left_pos(current_pos: tuple):
    new_pos = (current_pos[0] - 1, current_pos[1])
    return new_pos


def get_right_pos(current_pos: tuple):
    new_pos = (current_pos[0]+1, current_pos[1])
    return new_pos


def is_touching(h: tuple, t: tuple) -> bool:
    if h[0] - 1 <= t[0] <= h[0] + 1:
        if h[1] - 1 <= t[1] <= h[1] + 1:
            return True
    return False


def run_command(command: str):
    global head_pos
    global tail_pos
    global tail_spaces

    direction, distance = command.split()
    distance = int(distance)

    directions = {"U": get_up_pos, "D": get_down_pos,
                  "L": get_left_pos, "R": get_right_pos}

    for i in range(distance):
        head_pos = directions[direction](head_pos)
        if not is_touching(head_pos, tail_pos):
            x_dif = head_pos[0] - tail_pos[0]
            y_dif = head_pos[1] - tail_pos[1]
            if abs(x_dif) > 1:
                vector = x_dif / abs(x_dif)
                new_x = int(tail_pos[0] + x_dif - vector)
                tail_pos = (new_x, head_pos[1])
                tail_spaces.add(tail_pos)
            if abs(y_dif) > 1:
                vector = y_dif / abs(y_dif)
                new_y = int(tail_pos[1] + y_dif - vector)
                tail_pos = (head_pos[0], new_y)
                tail_spaces.add(tail_pos)
        # print(
        #     f"Step {i}. Head is at {head_pos}. Tail is at {tail_pos}. Tail has been to {tail_spaces}")

    return


def p1() -> str:
    # Solve code here, return string to submit

    for line in dataset:
        run_command(line)

    # print(tail_spaces)

    return f"{len(tail_spaces)}"


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
