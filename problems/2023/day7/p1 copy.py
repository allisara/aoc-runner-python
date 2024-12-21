from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "6440"

HAND_TYPES = {1: "High card", 2: "One pair",
              3: "Two pair", 4: "Three of a kind",
              5: "Full House", 6: "Four of a kind",
              7: "Five of a kind"}

CARD_VALUES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for c in "123456789":
    CARD_VALUES[c] = int(c)


class Hand():
    def __init__(self, type, cards, bid) -> None:
        self.type = type
        self.cards = cards
        self.bid = bid


def create_hand(input: str) -> object:
    hand_type = get_type(input[0])
    cards = get_cards(input[0])
    bid = int(input[1])

    hand = Hand(hand_type, cards, bid)

    return hand


def get_cards(input: str) -> list[int]:
    cards = []
    for c in input:
        if c == "A":
            cards.append(14)
        elif c == "K":
            cards.append(13)
        elif c == "Q":
            cards.append(12)
        elif c == "J":
            cards.append(11)
        elif c == "T":
            cards.append(10)
        else:
            cards.append(int(c))

    return cards


def get_type(input: str) -> int:
    cards = get_cards(input)
    distinct_cards = len(set(cards))

    if distinct_cards == 1:
        return 7  # 5 of a kind
    elif distinct_cards == 2:
        card_count = {}
        for c in set(cards):
            card_count[c] = 0
        for c in cards:
            card_count[c] += 1
            if card_count[c] == 4:
                return 6  # 4 of a kind
        return 5  # full house
    elif distinct_cards == 3:
        card_count = {}
        for c in set(cards):
            card_count[c] = 0
        for c in cards:
            card_count[c] += 1
            if card_count[c] == 3:
                return 4  # 3 of a kind
        return 3  # two pair
    elif distinct_cards == 4:
        return 2  # one pair
    elif distinct_cards == 5:
        return 1  # high card

    return -1


def p1() -> str:
    # Solve code here, return string to submit

    print(CARD_VALUES)

    return " "


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
