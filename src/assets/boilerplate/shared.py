import pathlib
from os import getenv

folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_SHORT") else "/dataset-short.txt"


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    return dataset


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        return _format_dataset(lines)
