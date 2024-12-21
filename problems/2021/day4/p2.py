from __future__ import annotations
from shared import get_dataset
from os import getenv
import math

dataset = get_dataset()
p2_test_case_answer: str = "1924"

GRID_SIZE = 5

balls = dataset.pop(0).split(",")
boards: list[Board] = []

answer = -1


class Board:
    def __init__(self, board_strs: list[str]) -> None:
        self.board_strs = board_strs
        self.numbers = self.parse_board_strs()

        self.still_playing = True
        self.unmarked_sum = sum(self.numbers)
        self.last_match = -1

        self.counts = {"mdd": 0, "mdu": 0}

        for i in range(GRID_SIZE):
            self.counts[f"r{i}"] = 0
            self.counts[f"c{i}"] = 0

    def update_board(self, ball_value: int):
        if self.still_playing:
            self.score_ball(ball_value)

            if self.is_solved():
                self.still_playing = False
                global answer
                answer = self.get_score()

    def score_ball(self, ball_value: int):
        value_pos = self.find_value(ball_value)

        if value_pos >= 0:
            self.last_match = ball_value
            self.unmarked_sum -= ball_value

            row = self.get_row(value_pos)
            self.counts[f"r{row}"] += 1

            col = self.get_col(value_pos)
            self.counts[f"c{col}"] += 1

            if self.is_in_mdd(row, col):
                self.counts["mdd"] += 1

            if self.is_in_mdu(row, col):
                self.counts["mdu"] += 1

        return

    def is_solved(self) -> bool:
        solved = False

        for value in self.counts.values():
            if value == 5:
                solved = True

        return solved

    def find_value(self, value: int) -> int:
        try:
            return self.numbers.index(value)
        except ValueError:
            return -1

    def get_row(self, num: int) -> int:
        row = math.floor(num / (GRID_SIZE))

        return row

    def get_col(self, num: int) -> int:
        col = num % GRID_SIZE
        return col

    def is_in_mdd(self, row: int, col: int) -> bool:
        return row == col

    def is_in_mdu(self, row: int, col: int) -> bool:

        return col == GRID_SIZE - row - 1

    def get_score(self) -> int:
        return self.last_match * self.unmarked_sum

    def parse_board_strs(self) -> list[int]:
        numbers = []

        for row in self.board_strs:
            row_strs = row.split()

            for num in row_strs:
                if num != ' ':
                    numbers.append(int(num))

        return numbers


def p2() -> str:
    # Solve code here, return string to submit
    for i in range(0, len(dataset), GRID_SIZE):
        board_input = []
        for j in range(GRID_SIZE):
            board_input.append(dataset[i + j])

        new_board = Board(board_input)
        boards.append(new_board)

    for ball in balls:
        for board in boards:
            board.update_board(int(ball))

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {
        'nothing' if p2_answer == '' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
