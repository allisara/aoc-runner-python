from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "4,6,3,5,6,3,5,2,1,0"

reg_a = dataset[0]
reg_b = dataset[1]
reg_c = dataset[2]
program = dataset[3:]


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


def p1() -> str:

    global reg_a
    global reg_b
    global reg_c
    global program

    output = ""

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        print(f"do {opcode} on {operand}")
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
            output = output + out(operand) + ","
        elif opcode == 6:
            bdv(operand)
        elif opcode == 7:
            cdv(operand)
        print(f"pointer:{i}, A: {reg_a}, B: {reg_b}, C: {reg_c}")
        i += 2

    print(output)
    output = output[:-1]

    return output


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {
        'nothing' if p1_answer == '' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
