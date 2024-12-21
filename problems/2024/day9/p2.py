from __future__ import annotations
from shared import get_dataset
from os import getenv


class File:
    def __init__(self, id: int, length: int, starts_at: int, buffer: int) -> None:
        self.id = id
        self.length = length
        self.starts_at = starts_at
        self.buffer = buffer
        self.next_file = id + 1

    def __str__(self) -> str:
        s = ""
        for __ in range(self.length):
            s = s + str(self.id)
        for __ in range(self.buffer):
            s = s + "."
        return s

    def __lt__(self, other: File) -> bool:
        return self.starts_at < other.starts_at


class Drive:
    # def __init__(self, files: list[File]) -> None:
    #     self.files = files
    #     self.files_to_move = list(reversed(self.files))

    def __init__(self, input: str) -> None:
        self.files: list[File] = []
        self.last_address = 0

        for i in range(0, len(input), 2):
            id_num = i // 2
            file_length = int(input[i])
            try:
                buffer = int(input[i + 1])
            except IndexError:
                buffer = 0
            new_file = File(id_num, file_length, self.last_address, buffer)
            self.files.append(new_file)
            self.last_address += file_length + buffer

        self.files_to_move = list(reversed(self.files))

    def __str__(self) -> str:
        s = ""
        for file in self.files:
            s = s + str(file)
        return s

    def move_file(self, from_index: int, to_index: int):
        file_to_move = self.files.pop(from_index)
        self.files[from_index - 1].buffer += file_to_move.length + \
            file_to_move.buffer
        file_to_move.buffer = self.files[to_index].buffer - file_to_move.length
        self.files[to_index].buffer = 0
        self.files.insert(to_index + 1, file_to_move)

    def find_gap(self, min_gap: int, stop_point: int) -> int:
        for i in range(stop_point):
            if self.files[i].buffer >= min_gap:
                return i
        return -1

    def condense_files(self):
        for file in self.files_to_move:
            right_index = self.files.index(file)
            left_index = self.find_gap(file.length, right_index)

            if left_index >= 0:
                self.move_file(right_index, left_index)

            # print(self)

    def checksum(self) -> int:
        answer = 0
        address = 0

        for file in self.files:
            for i in range(file.length):
                answer += (address + i) * file.id
            address += file.length + file.buffer

        return answer


dataset = get_dataset()
p2_test_case_answer: str = "2858"


def p2() -> str:
    # Solve code here, return string to submit

    drive = Drive(dataset[0])

    drive.condense_files()

    return f"{drive.checksum()}"


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
