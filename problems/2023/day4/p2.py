from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p2() -> str:
    # Solve code here, return string to submit

    total_cards = 0
    card_num = 1
    high_card = len(dataset)
    deck = {}

    for i in range(1, high_card+10):
        deck[i] = 1

    for card in dataset:

        in_winning = False
        in_card = False

        winning_numbers = []

        matches = 0

        input = card.split()

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
                    matches += 1

        for i in range(matches):
            deck[card_num + i + 1] += deck[card_num]

        card_num += 1

    for i in range(1, high_card + 1):
        total_cards += deck[i]

    return f"{total_cards}"


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
