import pathlib
from os import getenv

folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset-short.txt" if getenv("USE_SHORT") else "/dataset.txt"


def getDataset() -> "list[str]":
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        print(lines)
        return lines
