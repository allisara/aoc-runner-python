from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "12"


def get_outcome_score(game_pair: str) -> int:
    if "X" in game_pair:
        return 0
    elif "Y" in game_pair:
        return 3
    elif "Z" in game_pair:
        return 6

    return -999


def get_item_bonus(game_pair: str) -> int:
    if "X" in game_pair:
        if "A" in game_pair:
            return 3
        elif "B" in game_pair:
            return 1
        elif "C" in game_pair:
            return 2
        return -999
    elif "Y" in game_pair:
        if "A" in game_pair:
            return 1
        elif "B" in game_pair:
            return 2
        elif "C" in game_pair:
            return 3
        return -999
    elif "Z" in game_pair:
        if "A" in game_pair:
            return 2
        elif "B" in game_pair:
            return 3
        elif "C" in game_pair:
            return 1
        return -999

    return -999


def get_game_score(game_pair: str) -> int:

    return get_outcome_score(game_pair) + get_item_bonus(game_pair)


def get_tournament_score(input: "list[str]") -> int:

    score = 0

    for game in input:
        score += get_game_score(game)

    return score


def p2() -> str:
    # Solve code here, return string to submit
    score = get_tournament_score(dataset)

    return f"{score}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {'nothing' if p2_answer=='' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
