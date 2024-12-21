from shared import get_dataset
from os import getenv


dataset = get_dataset()
p1_test_case_answer: str = "ENTER TEST ANSWER HERE"


def get_distances(race_time: int) -> list[int]:
    distances = []

    for button_time in range(race_time):
        moving_time = race_time - button_time
        distances.append(moving_time * button_time)

    return distances


def p1() -> str:
    # Solve code here, return string to submit
    answer = 1

    time_str = dataset[0].split()
    time_str.pop(0)
    record_distance_str = dataset[1].split()
    record_distance_str.pop(0)

    races = []

    for i in range(len(time_str)):
        races.append((int(time_str[i]), int(record_distance_str[i])))

    for race in races:
        time, record = race
        winning_races = 0
        possible_distances = get_distances(time)

        for distance in possible_distances:
            if distance > record:
                winning_races += 1

        # print(winning_races)
        answer *= winning_races

    print(f"final answer: {answer}")

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
