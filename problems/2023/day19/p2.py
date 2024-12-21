from shared import get_dataset
from os import getenv


class Part_Range:
    def __init__(self) -> None:
        self.x_min = 1
        self.x_max = 4000
        self.m_min = 1
        self.m_max = 4000
        self.a_min = 1
        self.a_max = 4000
        self.s_min = 1
        self.s_max = 4000

    def __str__(self) -> str:
        return f"X: {self.x_min} to {self.x_max}\nM: {self.m_min} to {self.m_max}\nA: {self.a_min} to {self.a_max}\nS: {self.s_min} to {self.s_max}\n"

    def get_score(self) -> int:
        possible_xs = self.x_max - self.x_min + 1
        possible_ms = self.m_max - self.m_min + 1
        possible_as = self.a_max - self.a_min + 1
        possible_ss = self.s_max - self.s_min + 1

        return possible_xs * possible_ms * possible_as * possible_ss

    def is_split(self, criteria: str) -> bool:
        letter = criteria[0]
        value = int(criteria[2:])

        if letter == "x":
            return self.x_min < value < self.x_max
        elif letter == "m":
            return self.m_min < value < self.m_max
        elif letter == "a":
            return self.a_min < value < self.a_max
        elif letter == "s":
            return self.s_min < value < self.s_max

        print("Something's breaking in is_split()")

        return False


def make_copy(original: Part_Range) -> Part_Range:
    new_range = Part_Range()
    new_range.x_max = original.x_max
    new_range.x_min = original.x_min
    new_range.m_max = original.m_max
    new_range.m_min = original.m_min
    new_range.a_max = original.a_max
    new_range.a_min = original.a_min
    new_range.s_max = original.s_max
    new_range.s_min = original.s_min
    return new_range


dataset = get_dataset()
p2_test_case_answer: str = "167409079868000"

workflow_input: list[str] = dataset[0]
workflows: dict[str, str] = {}
for line in workflow_input:
    split_line: list[str] = line.split("{")
    workflows[split_line[0]] = split_line[1].replace("}", "")

all_ranges: list[Part_Range] = [Part_Range()]
accepted_ranges: list[Part_Range] = []


def split_range(original: Part_Range, criteria: str) -> list[Part_Range]:
    letter = criteria[0]
    op = criteria[1]
    value = int(criteria[2:])

    low_max = 0
    high_min = 0

    if op == ">":
        low_max = value
        high_min = value + 1
    elif op == "<":
        low_max = value - 1
        high_min = value

    low_range = make_copy(original)
    high_range = make_copy(original)

    if letter == "x":
        low_range.x_max = low_max
        high_range.x_min = high_min
    elif letter == "m":
        low_range.m_max = low_max
        high_range.m_min = high_min
    elif letter == "a":
        low_range.a_max = low_max
        high_range.a_min = high_min
    elif letter == "s":
        low_range.s_max = low_max
        high_range.s_min = high_min

    return [low_range, high_range]


def apply_rules(part_range: Part_Range, rules: str):
    all_rules = rules.split(",")

    for rule in all_rules:
        if ":" in rule:
            criteria = rule.split(":")[0]
            outcome: str = rule.split(":")[1]
            if part_range.is_split(criteria):
                new_ranges = split_range(part_range, criteria)
                low_range = new_ranges[0]
                high_range = new_ranges[1]

                if "<" in rule:
                    apply_rules(low_range, outcome)
                    apply_rules(high_range, rules)
                    return
                elif ">" in rule:
                    apply_rules(high_range, outcome)
                    apply_rules(low_range, rules)
                    return
        elif "R" in rule:
            return
        elif "A" in rule:
            accepted_ranges.append(part_range)
            return
        else:
            apply_rules(part_range, workflows[rule])

    return


def p2() -> str:
    # Solve code here, return string to submit

    total_range = Part_Range()

    apply_rules(total_range, "in")

    answer = 0

    for range in accepted_ranges:
        answer += range.get_score()

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
