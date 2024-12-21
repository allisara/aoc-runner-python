from shared import get_dataset, Hailstone
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "2"
TEST_RANGE_MIN = 200000000000000
TEST_RANGE_MAX = 400000000000000


def p1() -> str:
    # Solve code here, return string to submit

    answer = 0

    for i in range(len(dataset)):
        for j in range(i+1, len(dataset)):
            if dataset[i].xy_slope != dataset[j].xy_slope:
                # print(f"stones {i} and {j} are parallel")
                # else:
                intersection = dataset[i].get_xy_intersect(dataset[j])
                # print(f"Stones {i} and {j} intersect at {intersection}")
                if is_in_range(intersection) and dataset[i].is_future_xy(intersection) and dataset[j].is_future_xy(intersection):
                    # print("in range and in future")
                    answer += 1

    return f"{answer}"


def is_in_range(coords: tuple[float, float]) -> bool:
    x, y = coords
    return TEST_RANGE_MIN <= x <= TEST_RANGE_MAX and TEST_RANGE_MIN <= y <= TEST_RANGE_MAX


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
