from __future__ import annotations
from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "117440"

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


def run_program() -> str:

    global reg_a
    global reg_b
    global reg_c
    global program

    output = ""

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        # print(f"do {opcode} on {operand}")
        if opcode == 0:
            adv(operand)
            print(f"{i}: A = {reg_a}/ (2^combo({operand}))")
        elif opcode == 1:
            bxl(operand)
            print(f"{i} B = bitwise XOR of {reg_b} and {operand}")
        elif opcode == 2:
            bst(operand)
            print(f"{i}: B = combo({operand} % 8)")
        elif opcode == 3:
            if reg_a != 0:
                print(f"{i}: jump to {operand}")
                i = operand - 2
            else:
                print(f"{i}: A = 0, continue to {i + 1}")
        elif opcode == 4:
            bxc()
            print(f"{i}: B = bitwise XOR of B and C")
        elif opcode == 5:
            new_output = out(operand) + ","
            print(f"{i}: add {new_output} to output")
            output = output + new_output
        elif opcode == 6:
            bdv(operand)
            print(f"{i}: B = {reg_a}/ (2^combo({operand}))")
        elif opcode == 7:
            cdv(operand)
            print(f"{i}: B = {reg_a}/ (2^combo({operand}))")
        print(f"pointer:{i}, operand: {operand}, A: {
              reg_a} ({bin(reg_a)}), B: {reg_b} ({bin(reg_b)}), C: {reg_c} {bin(reg_c)}")
        print(f"output: {output}\n")
        i += 2

    output = output[:-1]

    return output


def p2() -> str:
    answer = ""

    # Solve code here, return string to submit
    global reg_a

    reg_a = 100

    run_program()

    # for i in range(1000):
    #     reg_a = i
    #     print(f"{i} ({oct(i)[2:]}): {run_program()}")

    # reg_a = 117440
    # print(f"{reg_a}: {run_program()}")

    # test = oct(reg_a - (reg_a % 8))[2:]
    # print(test)

    # reverse_output = ""

    # i = len(program) - 1

    # while i >= 0:
    #     reverse_output = reverse_output + str(program[i])
    #     i -= 1

    # # print(reverse_output)

    # # answer_str = reverse_output[1:] + "0"

    # # print(run_program())

    # # Program: 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0

    # octal_answer = "3553061345751420"
    # answer = int(octal_answer, 8)

    # print(answer)

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
