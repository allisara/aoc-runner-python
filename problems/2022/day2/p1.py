from shared import get_dataset, get_tournament_score
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "15"


def p1() -> str:
    # Solve code here, return string to submit

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

    score = get_tournament_score(dataset)

    return f"{score}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
