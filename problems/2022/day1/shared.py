import pathlib
from os import getenv
from pickle import TRUE


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    return dataset


class Elf:
    def __init__(self, start_index):
        self.calories: list[int] = []
        self.start_index = start_index

    def get_total_calories(self):
        return sum(self.calories)

    def print_elf(self):
        print(f"Start index: {self.start_index}")
        print(f"Calories: {self.calories}")
        print(f"Total Calories: {self.get_total_calories()}")


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        #lines = [s for s in d.read().splitlines(True) if s.strip()]
        lines = [s for s in d]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
