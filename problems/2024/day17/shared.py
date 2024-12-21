from __future__ import annotations
import pathlib
from os import getenv
import re


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: str):
    numbers = re.findall(r'\d+', dataset)
    return [int(num) for num in numbers]


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        # lines = [s for s in d.read().splitlines() if s.strip()]

        lines = d.read()
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")

        return _format_dataset(lines)
