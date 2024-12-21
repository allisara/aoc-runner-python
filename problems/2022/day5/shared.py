import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process

def get_stack(dataset: list[str], pos: int) -> list[str]:
    stack = []
    for row in dataset:
        if row[pos] is not " ":
            stack.append(row[pos])

    stack.reverse()

    return stack


def get_tops(stack: list[str]) -> str:
    tops = ""
    for column in stack:
        tops += column[-1]
    return tops


def _format_dataset(dataset: list[str]):
    first_half, second_half = dataset

    # Format first half
    start_columns = first_half.split("\n")
    start_columns.pop()
    number_of_columns = (len(start_columns[0]) + 1) // 4
    crates = []

    for i in range(number_of_columns):
        crates.append(get_stack(start_columns, i * 4 + 1))

    # format second half
    command_ints = [int(s) for s in second_half.split() if s.isdigit()]
    instructions = []
    for i in range(0, len(command_ints), 3):
        instructions.append(
            [command_ints[i], command_ints[i+1], command_ints[i+2]])

    dataset_tuple: tuple = (crates, instructions)
    return dataset_tuple


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    dataset = open(folder + file, 'r')
    raw_input = dataset.read().split("\n\n")
    return _format_dataset(raw_input)
    # return raw_input
