import pathlib
from os import getenv
from dataclasses import dataclass


@dataclass
class Plant:
    height: int
    visible: bool
    scenic_score: int = 0

    def __str__(self) -> str:
        return f"Height: {self.height}\nIs visible?: {self.visible}"

# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def count_visible(plants: list[list[Plant]]) -> int:
    counter = 0
    for row in plants:
        for plant in row:
            if plant.visible:
                counter += 1
    return counter


def _format_dataset(dataset: "list[str]"):
    plants: list[list[Plant]] = []
    for row in dataset:
        plant_row: list[Plant] = []
        for c in row:
            new_plant = Plant(int(c), False)
            plant_row.append(new_plant)
        plants.append(plant_row)

    return plants


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
