import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def bisect_string(contents):
    compartments = []
    middle = int(len(contents) / 2)

    compartments.append(contents[:middle])
    compartments.append(contents[middle:])

    return compartments


def get_intersection(compartments):
    intersection = set(compartments[0]).intersection(compartments[1])
    intersection = list(intersection)
    return intersection[0]


def get_priority(item):
    priority = ord(item)

    if priority >= 65 and priority <= 90:
        priority -= 38
    elif priority >= 97 and priority <= 122:
        priority -= 96

    return priority


# Format dataset for p2
def _format_dataset(dataset: "list[str]"):

    return dataset


# Format dataset for p1
#
# def _format_dataset(dataset: "list[str]"):
#
#    compartments = []
#
#    for pack in dataset:
#        compartments.append(get_priority(
#            get_intersection(bisect_string(pack))))
#
#    return compartments

# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
