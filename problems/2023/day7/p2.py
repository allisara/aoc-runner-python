from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "5905"

HAND_TYPES = {1: "High card", 2: "One pair",
              3: "Two pair", 4: "Three of a kind",
              5: "Full House", 6: "Four of a kind",
              7: "Five of a kind"}

CARD_VALUES = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
for c in "23456789":
    CARD_VALUES[c] = int(c)


class Hand():
    def __init__(self, input_card_str, input_bid_str) -> None:
        self.card_str = input_card_str
        self.bid = int(input_bid_str)
        self.card_values = self.get_cards()
        self.type = self.get_type()
        self.points = self.get_points()

    def __str__(self) -> str:
        hand_str = self.card_str + \
            " (" + HAND_TYPES[self.type] + ")  Bid: " + str(self.bid)
        return hand_str

    def get_points(self) -> int:
        points = self.type

        for c in self.card_values:
            points *= 100
            points += c

        return points

    def get_type_wild(self) -> int:
        j_count = 0
        tames = []

        for c in self.card_str:
            if c == "J":
                j_count += 1
            else:
                tames.append(c)

        distinct_tames = len(set(tames))

        if j_count == 5 or distinct_tames == 1:
            return 7  # 5 of a kind
        elif distinct_tames == 4:
            return 2  # one pair
        elif distinct_tames == 3:
            return 4  # 3 of a kind
        elif distinct_tames == 2:
            if j_count == 3:
                return 6  # 4 of a kind
            elif j_count == 2:
                return 6  # 4 of a kind
            elif j_count == 1:
                first_tame = tames[0]
                instances = 0
                for c in tames:
                    if c == first_tame:
                        instances += 1
                if instances == 2:
                    return 5  # full house
                else:
                    return 6  # 4 of a kind

        return -1

    def get_type(self) -> int:

        if "J" in self.card_str:
            return self.get_type_wild()

        distinct_cards = len(set(self.card_values))
        if distinct_cards == 1:
            return 7  # 5 of a kind
        elif distinct_cards == 2:
            card_count = {}
            for c in set(self.card_values):
                card_count[c] = 0
            for c in self.card_values:
                card_count[c] += 1
                if card_count[c] == 4:
                    return 6  # 4 of a kind
            return 5  # full house
        elif distinct_cards == 3:
            card_count = {}
            for c in set(self.card_values):
                card_count[c] = 0
            for c in self.card_values:
                card_count[c] += 1
                if card_count[c] == 3:
                    return 4  # 3 of a kind
            return 3  # two pair
        elif distinct_cards == 4:
            return 2  # one pair
        elif distinct_cards == 5:
            return 1  # high card

        return -1

    def get_cards(self) -> list[int]:
        card_list = []
        for c in self.card_str:
            card_list.append(CARD_VALUES[c])

        return card_list


def p2() -> str:
    # Solve code here, return string to submit

    all_hands = []

    for hand in dataset:
        input = hand.split()
        new_hand = Hand(input[0], input[1])
        all_hands.append(new_hand)

    all_hands = sorted(all_hands, key=lambda hand: hand.points)

    answer = 0
    rank = 1

    for hand in all_hands:
        print(hand)
        answer += hand.bid * rank
        rank += 1

    return f"{answer}"


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
