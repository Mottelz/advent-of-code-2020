from utils import read_file_by_line
from typing import List
from copy import deepcopy


def get_new_cell_state(cell: str, neighbours: List[str]) -> str:
    if cell == 'L' and neighbours.count('#') == 0:
        return '#'
    elif cell == '#' and neighbours.count('#') >= 4:
        return 'L'
    else:
        return cell


def get_surrounding_cells(row: int, col: int, seating_chart: List[List[str]]) -> List[str]:
    surrounding_cells = []
    check_up = row - 1 >= 0
    check_down = row + 1 < len(seating_chart)
    check_left = col - 1 >= 0
    check_right = col + 1 < len(seating_chart[row])

    if check_up:
        surrounding_cells.append(seating_chart[row-1][col])

    if check_down:
        surrounding_cells.append(seating_chart[row+1][col])

    if check_left:
        surrounding_cells.append(seating_chart[row][col-1])

    if check_right:
        surrounding_cells.append(seating_chart[row][col+1])

    if check_up and check_left:
        surrounding_cells.append(seating_chart[row-1][col-1])

    if check_up and check_right:
        surrounding_cells.append(seating_chart[row-1][col+1])

    if check_down and check_left:
        surrounding_cells.append(seating_chart[row + 1][col - 1])

    if check_down and check_right:
        surrounding_cells.append(seating_chart[row + 1][col + 1])

    return surrounding_cells


def get_stable_state(seating_chart: List[List[str]]) -> List[List[str]]:
    no_state_change = False
    iterations = 0
    while not no_state_change:
        temp_chart = deepcopy(seating_chart)
        no_state_change = True
        for row in range(len(seating_chart)):
            for col in range(len(seating_chart[row])):
                cell = seating_chart[row][col]
                neighbours = get_surrounding_cells(row, col, seating_chart)
                new_cell = get_new_cell_state(cell, neighbours)
                if new_cell != cell:
                    no_state_change = False
                    temp_chart[row][col] = new_cell
        seating_chart = deepcopy(temp_chart)
        iterations += 1
    return seating_chart


def generate_seating_chart(raw: List[str]) -> List[List[str]]:
    seating_chart = [[cell for cell in row] for row in raw]
    return seating_chart


def pretty_chart(chart: List[List[str]]) -> str:
    out = ""
    for row in chart:
        for seat in row:
            out += seat
        out += "\n"
    return out


def get_occupied_count(chart: List[List[str]]) -> int:
    count = 0
    for row in chart:
        count += row.count('#')
    return count


def main():
    data = read_file_by_line('input.txt')
    seating_chart = generate_seating_chart(data)
    stable_chart = get_stable_state(seating_chart)
    part1 = get_occupied_count(stable_chart)
    print(part1)


if __name__ == "__main__":
    main()
