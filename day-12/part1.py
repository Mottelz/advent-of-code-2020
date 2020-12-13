from ship import Ship
from utils import read_file_by_line


def parse_instruction(raw: str) -> (str, int):
    return raw[0], eval(raw[1:])


def activate_instruction(ship, instruction, val):
    if instruction == 'F':
        ship.move_forward(val)
        return ship

    elif instruction == 'R':
        ship.turn_right(val)
        return ship

    elif instruction == 'L':
        ship.turn_left(val)
        return ship

    elif instruction == 'N':
        ship.move_north(val)
        return ship

    elif instruction == 'S':
        ship.move_south(val)
        return ship

    elif instruction == 'E':
        ship.move_east(val)
        return ship

    elif instruction == 'W':
        ship.move_west(val)
        return ship


def main():
    ferry = Ship()
    directions = read_file_by_line('input.txt')
    for raw in directions:
        inst, val = parse_instruction(raw)
        ferry = activate_instruction(ferry, inst, val)
    print(ferry)


if __name__ == "__main__":
    main()
