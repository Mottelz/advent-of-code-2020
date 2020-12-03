from utils import read_file_by_line
from typing import List


def parse_line(line: str) -> List[bool]:
    out = []
    for char in line:
        out.append(char == '#')
    return out


def part_one_count(mountain: List[List[bool]], jump_distance: int, starting_pos: int) -> int:
    count = 0  # Number of trees hit
    current_pos = starting_pos  # starting position
    for line in mountain:
        current_pos += jump_distance
        count = count + 1 if line[current_pos % len(line)] else count
    return count


def part_two_count(mountain: List[List[bool]], jump_right_distance: int, jump_down_distance: int,
                   starting_pos: int) -> int:
    count = 0  # Number of trees hit
    current_pos = starting_pos  # starting position
    for i in range(jump_down_distance, len(mountain), jump_down_distance):
        current_pos += jump_right_distance
        count = count + 1 if mountain[i][current_pos % len(mountain[i])] else count
    print(count)
    return count


def solution_one():
    data = read_file_by_line('input.txt')
    mountain = []
    for line in data:
        mountain.append(parse_line(line))
    print(part_two_count(mountain, 3, 1, 0))
    mountain.pop(0)
    print(part_one_count(mountain, 3, 0))


def solution_two():
    data = read_file_by_line('input.txt')
    mountain = []
    for line in data:
        mountain.append(parse_line(line))
    total = part_two_count(mountain, 1, 1, 0) * \
            part_two_count(mountain, 3, 1, 0) * \
            part_two_count(mountain, 5, 1, 0) * \
            part_two_count(mountain, 7, 1, 0) * \
            part_two_count(mountain, 1, 2, 0)
    print(total)


solution_two()
