from shared import get_dataset, Elf
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "24000"


def create_elf(start_index, dataset):
    elf = Elf(start_index)

    pos = start_index

    while (pos < len(dataset)):
        if (dataset[pos] != "\n"):
            elf.calories.append(int(dataset[pos]))
        else:
            pos = len(dataset)
        pos += 1

    return elf


def p1() -> str:
    # Solve code here, return string to submit

    elf_indices = [0]
    elves = []

    for i in range(len(dataset)):
        if dataset[i] == "\n":
            elf_indices.append(i+1)

    for value in elf_indices:
        new_elf = create_elf(value, dataset)
       # new_elf.print_elf()
        elves.append(new_elf)

    max_total_cal = 0

    for elf in elves:
        if (elf.get_total_calories() > max_total_cal):
            max_total_cal = elf.get_total_calories()

    return str(max_total_cal)


# pos = self.start_index

#         while (pos < len(dataset)):
#             if (dataset[pos] != "\n"):
#                 self.calories.append(int(dataset[pos]))
#             else:
#                 pos = len(dataset)
#             pos += 1


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
