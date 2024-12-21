from shared import get_dataset
from os import getenv
import re


class Part:
    def __init__(self, input: str) -> None:
        self.values = re.findall(r"\d+", input)

        self.x: int = int(self.values[0])
        self.m: int = int(self.values[1])
        self.a: int = int(self.values[2])
        self.s: int = int(self.values[3])

    def __str__(self) -> str:
        return f"X: {self.x}\nM: {self.m}\nA: {self.a}\nS: {self.s}\n"

    def get_score(self) -> int:
        return self.x + self.m + self.a + self.s

    def run_check(self, criteria: str) -> bool:
        letter = criteria[0]
        op = criteria[1]
        value = int(criteria[2:])

        num_to_check = 0
        if letter == "x":
            num_to_check = self.x
        elif letter == "m":
            num_to_check = self.m
        elif letter == "a":
            num_to_check = self.a
        elif letter == "s":
            num_to_check = self.s

        if op == ">":
            return num_to_check > value
        elif op == "<":
            return num_to_check < value

        print("Something's breaking in run_check()")

        return False


dataset = get_dataset()
p1_test_case_answer: str = "19114"

workflow_input: list[str] = dataset[0]
parts_input: list[str] = dataset[1]

workflows: dict[str, str] = {}
for line in workflow_input:
    split_line: list[str] = line.split("{")
    workflows[split_line[0]] = split_line[1].replace("}", "")


parts = []
for line in parts_input:
    parts.append(Part(line))

accepted_parts: list[Part] = []


def apply_rules(part: Part, rules: str):
    all_rules = rules.split(",")

    for rule in all_rules:
        if ":" in rule:
            criteria = rule.split(":")[0]
            outcome: str = rule.split(":")[1]
            if part.run_check(criteria):
                apply_rules(part, outcome)
                return
        elif "R" in rule:
            return
        elif "A" in rule:
            accepted_parts.append(part)
            return
        else:
            apply_rules(part, workflows[rule])

    return


def p1() -> str:
    # Solve code here, return string to submit

    for part in parts:
        apply_rules(part, workflows["in"])

    answer = 0

    for part in accepted_parts:
        # print(part.get_score())
        # print(part)
        answer += part.get_score()

    return f"{answer}"


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
