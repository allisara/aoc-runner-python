from shared import get_dataset
from os import getenv
import math

dataset = get_dataset()
p2_test_case_answer: str = "ENTER TEST ANSWER HERE"


def p2() -> str:
    # Solve code here, return string to submit
    race_time_str = ""
    record_time_str = ""

    time_strs = dataset[0].split()
    record_strs = dataset[1].split()

    for i in range(1, len(time_strs)):
        race_time_str += time_strs[i]
        record_time_str += record_strs[i]

    race_time = int(race_time_str)
    record_distance = int(record_time_str)

    # distance = x * (total_time - x)
    # x^2 - total_time * x + distance = 0

    max_time = int(
        (race_time + math.sqrt(race_time**2 - 4 * record_distance)) / 2)
    min_time = int(
        (race_time - math.sqrt(race_time**2 - 4 * record_distance)) / 2)

    answer = max_time - min_time

    print(f"{answer} ways to win between {min_time} (exclusive) and {max_time} (inclusive)")

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
