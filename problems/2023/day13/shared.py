import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]") -> list[list[str]]:
    all_blocks = []

    for block in dataset:
        all_blocks.append(block.split())

    return all_blocks


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().split("\n\n")]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
