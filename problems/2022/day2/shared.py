import pathlib
from os import getenv
from time import gmtime


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    return dataset


def get_outcome_score(game_pair: str) -> int:
    if game_pair == "A Z" or game_pair == "B X" or game_pair == "C Y":
        return 0
    elif game_pair == "A X" or game_pair == "B Y" or game_pair == "C Z":
        return 3
    elif game_pair == "A Y" or game_pair == "B Z" or game_pair == "C X":
        return 6

    return -999


def get_item_bonus(game_pair: str) -> int:
    if "X" in game_pair:
        return 1
    elif "Y" in game_pair:
        return 2
    elif "Z" in game_pair:
        return 3

    return 0


def get_game_score(game_pair: str) -> int:

    return get_outcome_score(game_pair) + get_item_bonus(game_pair)


def get_tournament_score(input: "list[str]") -> int:

    score = 0

    for game in input:
        score += get_game_score(game)

    return score


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
