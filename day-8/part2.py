from utils import read_file_by_line
from typing import List
import copy


def read_instruction(raw: str) -> (str, int):
    instruction = raw.split(' ')
    return instruction[0], eval(instruction[1])


def run_program(program: List[str]) -> (int, bool):
    accumulator = 0
    lines_read = []
    current_line = 0
    while True:
        if current_line > len(program) - 1:
            return accumulator, True
        op, val = read_instruction(program[current_line])
        if current_line in lines_read:
            return accumulator, False
        elif op == 'nop':
            lines_read.append(current_line)
            current_line += 1
        elif op == 'acc':
            accumulator += val
            lines_read.append(current_line)
            current_line += 1
        elif op == 'jmp':
            lines_read.append(current_line)
            current_line += val


def correct_program(program: List[str]) -> int:
    for i in range(len(program)):
        temp_program = copy.deepcopy(program)
        op, val = read_instruction(temp_program[i])
        if op == 'nop':
            temp_program[i] = f"jmp {val}"
            output_val, status = run_program(temp_program)
            if status:
                return output_val
        elif op == 'jmp':
            temp_program[i] = f"nop {val}"
            output_val, status = run_program(temp_program)
            if status:
                return output_val


def main():
    program = read_file_by_line('input.txt')
    part2 = correct_program(program)
    print(part2)


if __name__ == "__main__":
    main()