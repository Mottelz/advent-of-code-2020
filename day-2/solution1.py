from typing import List


# Read in file
def read_in_files(filename: str) -> List[str]:
    with open(filename) as file:
        data = file.read().splitlines()
    return data


# Parse each line
def parse_line(line: str) -> (int, int, str, str):
    line = line.replace(':', '')
    line = line.replace('-', ' ')
    split_line = line.split()
    return eval(split_line[0]), eval(split_line[1]), split_line[2], split_line[3]


# Validate password for part I
def validate_password_for_sleds(min_count: int, max_count: int, letter: str, password: str) -> bool:
    count = len([a for a in password if a == letter])
    return min_count <= count <= max_count


# Validate password for part II
def validate_password_for_toboggan(pos1: int, pos2: int, letter: str, password: str) -> bool:
    return (password[pos1-1] == letter) ^ (password[pos2-1] == letter)


# Solution to part 1
def part1():
    data = read_in_files("input.txt")
    count = 0
    for line in data:
        min_val, max_val, letter, pword = parse_line(line)
        if validate_password_for_sleds(min_val, max_val, letter, pword):
            count += 1
    print(count)


# Solution to part 2
def part2():
    data = read_in_files("input.txt")
    count = 0
    for line in data:
        pos1, pos2, letter, pword = parse_line(line)
        if validate_password_for_toboggan(pos1, pos2, letter, pword):
            count += 1
    print(count)
