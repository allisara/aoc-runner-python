from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p1() -> str:
    # Solve code here, return string to submit

    total_points = 0

    for card in dataset:
        points = 0
        match_power = -1
        in_winning = False
        in_card = False

        winning_numbers = []

        input = card.replace("  ", " ").split(" ")

        for word in input:
            if ":" in word:
                in_winning = True
            elif in_winning:
                if word == "|":
                    in_winning = False
                    in_card = True
                else:
                    winning_numbers.append(int(word))
            elif in_card:
                num_to_check = int(word)
                if num_to_check in winning_numbers:
                    match_power += 1

        if match_power >= 0:
            points += 2 ** match_power

        total_points += points

    return f"{total_points}"


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
