from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "145"


class Box():
    def __init__(self, box_num) -> None:
        self.number: int = box_num
        self.lenses: list[str] = []
        self.focal_lengths: dict[str, int] = {}

    def add_lens(self, label: str, focal_length: int) -> None:
        self.focal_lengths[label] = focal_length
        if label not in self.lenses:
            self.lenses.append(label)
        return

    def remove_lens(self, label: str) -> None:
        if label in self.lenses:
            self.lenses.remove(label)
        return

    def __str__(self) -> str:
        string = f"Box {self.number}: "

        for lens in self.lenses:
            string += f"[{lens} {self.focal_lengths[lens]}] "
        return string

    def get_box_score(self) -> int:
        score = 0
        box_value = self.number + 1

        for i in range(len(self.lenses)):
            slot_val = i + 1
            focal_val = self.focal_lengths[self.lenses[i]]
            score += box_value * slot_val * focal_val

        return score


boxes: list[Box] = []
for i in range(256):
    boxes.append(Box(i))


def p2() -> str:
    # Solve code here, return string to submit

    for line in dataset:
        if "=" in line:
            run_add_op(line)
        elif "-" in line:
            run_remove_op(line)

    answer = 0

    for box in boxes:
        if len(box.lenses) > 0:
            print(box)
            answer += box.get_box_score()

    return f"{answer}"


def convert_label(string: str) -> int:
    current_value = 0

    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


def run_add_op(command: str) -> None:
    command_parts = command.split("=")
    label = command_parts[0]
    focal_length = int(command_parts[1])
    hash_num = convert_label(label)
    boxes[hash_num].add_lens(label, focal_length)
    return


def run_remove_op(command: str) -> None:
    label = command[0:-1]
    hash_num = convert_label(label)
    boxes[hash_num].remove_lens(label)
    return


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
