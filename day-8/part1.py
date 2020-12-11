from utils import read_file_by_line
from typing import List


def read_instruction(raw: str) -> (str, int):
    instruction = raw.split(' ')
    return instruction[0], eval(instruction[1])


def run_program(program: List[str]) -> int:
    accumulator = 0
    lines_read = []
    current_line = 0
    while True:
        op, val = read_instruction(program[current_line])
        # If we're repeating, break.
        if current_line in lines_read:
            return accumulator
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


def main():
    program = read_file_by_line('input.txt')
    part1 = run_program(program)
    print(part1)


if __name__ == "__main__":
    main()