import pathlib
from os import getenv


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):

    return [int(i) for i in dataset]

    # list = []

    # for item in dataset:
    #     list.append(int(item))

    # return list


def get_module_fuel(mass: int):
    fuel = int(mass / 3) - 2

    return fuel


def get_module_fuel_total(mass: int):
    fuel = get_module_fuel(mass)
    total_fuel = fuel

    if get_module_fuel(fuel) > 0:
        total_fuel += get_module_fuel_total(fuel)

    return total_fuel


def get_fuels(list):
    fuels = []

    for mass in list:
        fuels.append(get_module_fuel_total(mass))

    return fuels


def add_fuels(dataset):
    fuels = get_fuels(dataset)
    total = sum(fuels)
    return total


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
