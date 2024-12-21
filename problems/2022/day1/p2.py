from shared import get_dataset, Elf
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "45000"


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


def p2() -> str:
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

    calories = []
    top_three = []

    for elf in elves:
        calories.append(elf.get_total_calories())

    calories.sort(reverse=True)
    return str(sum(calories[:3]))

    # for i in range(0, 3, 1):
    #     top_three.append(calories[i])

    # top_three_sum = sum(top_three)

    # print(top_three)

    # return str(top_three_sum)


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
