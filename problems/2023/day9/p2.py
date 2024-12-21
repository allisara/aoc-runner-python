from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "2"


class Sequence():
    def __init__(self, input: list[str]) -> None:
        self.source = input
        self.full_sequence = []

        self.build_sequence()
        self.extrapolate()

    def get_value(self) -> int:
        # value = 0
        # for line in self.full_sequence:
        #     value += line[-1]
        return self.full_sequence[0][0]

    def extrapolate(self):
        self.full_sequence[-1].insert(0, 0)

        for i in range(2, len(self.full_sequence) + 1):
            original = self.full_sequence[-i][0]
            num_to_subtract = self.full_sequence[-i + 1][0]
            self.full_sequence[-i].insert(0, original - num_to_subtract)

        return

    def build_sequence(self):
        self.full_sequence.append(self.get_first_sequence())
        # print(self.full_sequence)
        self.add_next_row()
        # print(self.full_sequence)

        is_penultimate = (set(self.get_next_deltas()) == {0})

        if is_penultimate:
            self.add_next_row()
            still_building = False
        else:
            still_building = True

        while still_building:
            # print(self.full_sequence)
            self.add_next_row()
            # if len(self.get_next_deltas()) == 1:
            if set(self.get_next_deltas()) == {0}:
                self.add_next_row()
                still_building = False
        return

    def __str__(self) -> str:
        seq_str = ""
        offset = ""
        for line in self.full_sequence:
            seq_str += offset + str(line) + "\n"
            offset += "  "
        seq_str += f"Value: {self.get_value()}\n"
        return seq_str

    def get_first_sequence(self) -> list[list[int]]:
        # sequence = []
        next_line = []

        for value in self.source:
            next_line.append(int(value))

        # sequence.append(next_line)

        return next_line

    def add_next_row(self):
        next_row = self.get_next_deltas()
        self.full_sequence.append(next_row)

    def get_next_deltas(self) -> list[int]:
        next_deltas = []
        bottom_line = self.full_sequence[-1]

        for i in range(len(bottom_line) - 1):
            delta = bottom_line[i+1] - bottom_line[i]
            next_deltas.append(delta)

        return next_deltas


def p2() -> str:
    # Solve code here, return string to submit

    sequences = []
    answer = 0

    for line in dataset:
        sequences.append(Sequence(line))

    for sequence in sequences:
        # print(sequence)
        answer += sequence.get_value()

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
