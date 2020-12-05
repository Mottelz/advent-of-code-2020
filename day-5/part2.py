from utils import read_file_by_line
from part1 import bin_str_to_int, ticket_to_bin

if __name__ == '__main__':
    possibles = [n for n in range(55, 907)]
    data = read_file_by_line('input.txt')
    for ticket in data:
        possibles.remove(bin_str_to_int(ticket_to_bin(ticket)))
    print(possibles)
