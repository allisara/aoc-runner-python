from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "117440"

reg_a = dataset[0]
reg_b = dataset[1]
reg_c = dataset[2]
program = dataset[3:]
program_str = ",".join(map(str, program))


def combo(operand: int) -> int:
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    else:
        print(f"Invalid operand: {operand}")
        return -1


def adv(operand: int):
    global reg_a
    reg_a = int(reg_a / (2**combo(operand)))


def bxl(operand: int):
    global reg_b
    reg_b = reg_b ^ operand


def bst(operand: int):
    global reg_b
    reg_b = combo(operand) % 8


def bxc():
    global reg_b
    global reg_c
    reg_b = reg_b ^ reg_c


def out(operand: int) -> str:
    return str(combo(operand) % 8)


def bdv(operand: int):
    global reg_a
    global reg_b
    reg_b = int(reg_a / (2**combo(operand)))


def cdv(operand: int):
    global reg_a
    global reg_c
    reg_c = int(reg_a / (2**combo(operand)))


def run_program(test: bool) -> str:

    global reg_a
    global reg_b
    global reg_c
    global program
    global program_str

    output = ""

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3:
            if reg_a != 0:
                i = operand - 2
        elif opcode == 4:
            bxc()
        elif opcode == 5:
            new_output = out(operand) + ","
            output = output + new_output
            if test and program_str.find(output[:-1]) != 0:
                return "wrong output"
        elif opcode == 6:
            bdv(operand)
        elif opcode == 7:
            cdv(operand)

        i += 2

    output = output[:-1]

    return output


def p2() -> str:
    global reg_a
    global reg_b
    global reg_c

    answer = ""

    for i in range(10000):
        reg_a = i
        reg_b = 0
        reg_c = 0
        output = run_program(False)
        if output == program_str:
            answer = f"{i}"
            print(f"{answer}")
            break
        # if output != "wrong output":
        #     print(f"output at {i} ({oct(i)}): {output}")

        if i % 8 == 0:
            print(f"output at {i} ({oct(i)}): {output}")

    return answer


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
