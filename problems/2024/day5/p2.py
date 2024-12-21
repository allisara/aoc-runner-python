from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "123"

raw_rules = dataset[0].splitlines()
raw_updates = dataset[1].splitlines()


class Page:
    def __init__(self, title: str) -> None:
        self.title = title
        self.pages_before: set[str] = set()
        self.pages_after: set[str] = set()

    def __str__(self) -> str:
        return f"Page '{self.title}':\n Pages before: {self.pages_before}\n Pages after: {self.pages_after}"

    def __lt__(self, other: Page) -> bool:
        return len(self.pages_before) < len(other.pages_before)


def get_updated_page(new_page_title: str, pages_in_update: list[str], page_master: Page) -> Page:
    new_page = Page(new_page_title)
    pages_in_update_set = set(pages_in_update)

    new_page.pages_before = pages_in_update_set & page_master.pages_before
    new_page.pages_after = pages_in_update_set & page_master.pages_after

    return new_page


all_pages: dict[str, Page] = {}

for rule in raw_rules:
    titles = rule.split("|")

    try:
        all_pages[titles[0]].pages_after.add(titles[1])
    except KeyError:
        new_page = Page(titles[0])
        new_page.pages_after.add(titles[1])
        all_pages[titles[0]] = new_page

    try:
        all_pages[titles[1]].pages_before.add(titles[0])
    except KeyError:
        new_page = Page(titles[1])
        new_page.pages_before.add(titles[0])
        all_pages[titles[1]] = new_page


unordered_updates: list[list[Page]] = []

for line in raw_updates:

    titles_in_line = line.split(",")

    pages_in_line: list[Page] = []
    positions: list[int] = []

    for title in titles_in_line:
        new_page = get_updated_page(title, titles_in_line, all_pages[title])
        pages_in_line.append(new_page)
        positions.append(len(new_page.pages_before))

    if positions != sorted(positions):
        unordered_updates.append(pages_in_line)


def p2() -> str:

    answer = 0

    for line in unordered_updates:
        sorted_line: list[Page] = sorted(line)
        middle_index = len(sorted_line) // 2
        middle_num = int(sorted_line[middle_index].title)
        answer += middle_num

    # for p in unordered_updates[0]:
    #     print(f"{p.title}")

    # ordered_updates: list[Page] = sorted(unordered_updates[0])

    # print("------")

    # for p in ordered_updates:
    #     print(f"{p.title}")

    # print("_________")

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {
        'nothing' if p2_answer == '' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
