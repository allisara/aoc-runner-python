from shared import get_dataset, get_priority
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "70"


def make_groups(dataset):
    groups = []

    for i in range(0, len(dataset), 3):
        groups.append(dataset[i: i+3])

    return groups


def get_common_item(groups):
    common_item = set(groups[0]) & set(groups[1]) & set(groups[2])
    common_item = list(common_item)
    return common_item[0]


def get_common_items(groups):
    common_items = []

    for group in groups:
        common_items.append(get_common_item(group))

    return common_items


def p2() -> str:
    # Solve code here, return string to submit
    groups = make_groups(dataset)
    badges = get_common_items(groups)

    group_priority = []

    for badge in badges:
        group_priority.append(get_priority(badge))

    # print(group_priority)

    return f"{sum(group_priority)}"


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
