from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "21"


def p1() -> str:
    # Solve code here, return string to submit

    answer = 0

    for line in dataset:
        answer += count_valid_arrangements(line)

    return f"{answer}"


def count_valid_arrangements(record_line: tuple[str, list[int]]) -> int:
    valid_arrangements = []

    record, key = record_line

    possible_arrangements = get_possibilities(record)

    for arrangement in possible_arrangements:
        if matches_key(arrangement, key):
            valid_arrangements.append(arrangement)

    return len(valid_arrangements)


def get_possibilities(record: str) -> list[str]:
    possibilities = []

    if "?" not in record:
        possibilities += [record]

    else:
        option_a = record.replace("?", "#", 1)
        possibilities += get_possibilities(option_a)

        option_b = record.replace("?", ".", 1)
        possibilities += get_possibilities(option_b)

    return possibilities


def matches_key(record: str, key: list[int]) -> bool:
    record = record.replace(".", " ")
    blocks = record.split()

    block_lengths = []
    for block in blocks:
        block_lengths.append(len(block))

    return block_lengths == key


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
