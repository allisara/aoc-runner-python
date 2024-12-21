from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "36"

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
visited: set[tuple[int, int]] = set()
visited.add((0, 0))


def is_touching(h: tuple, t: tuple) -> bool:
    if h[0] - 1 <= t[0] <= h[0] + 1:
        if h[1] - 1 <= t[1] <= h[1] + 1:
            return True
    return False


def follow(h: tuple[int, int], t: tuple[int, int]) -> tuple[int, int]:
    if is_touching(h, t):
        return t

    hx, hy = h
    tx, ty = t

    if hx - 2 >= tx:
        tx += 1
    elif hx + 2 <= tx:
        tx -= 1

    if hy - 2 >= ty:
        ty += 1
    elif hy + 2 <= ty:
        ty -= 1

    return (tx, ty)


def move_head(pos: tuple[int, int], dir: str) -> tuple[int, int]:
    delta_x, delta_y = directions[dir]
    new_pos = (pos[0] + delta_x, pos[1]+delta_y)
    return new_pos


def move_snake(snake: list[tuple[int, int]], dir: str) -> list[tuple[int, int]]:
    for i in range(len(snake)):
        if i == 0:
            snake[i] = move_head(snake[i], dir)
        else:
            snake[i] = follow(snake[i-1], snake[i])
        visited.add(snake[9])

    return snake


def p2() -> str:
    # Solve code here, return string to submit
    snake: list[tuple[int, int]] = []
    for i in range(10):
        snake.append((0, 0))

    for line in dataset:
        direction, distance = line.split()
        for j in range(int(distance)):
            snake = move_snake(snake, direction)

    return f"{len(visited)}"


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
