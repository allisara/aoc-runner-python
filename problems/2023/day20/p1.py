from shared import get_dataset, Module
from os import getenv

all_modules = get_dataset()
p1_test_case_answer: str = "11687500"


def p1() -> str:
    # Solve code here, return string to submit

    low_pulses = 0
    high_pulses = 0

    for i in range(1000):
        pulse_queue = [(-1, "button", "broadcaster")]

        while len(pulse_queue) > 0:
            this_pulse = pulse_queue[0]
            pulse_queue = pulse_queue[1:]

            if this_pulse[0] > 0:
                high_pulses += 1
            else:
                low_pulses += 1

            pulse_queue += all_modules[this_pulse[2]
                                       ].get_next_pulses(this_pulse)
            # print(pulse_queue)

    return f"{low_pulses * high_pulses}"


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
