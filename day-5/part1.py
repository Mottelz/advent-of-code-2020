from utils import read_file_by_line


def bin_str_to_int(ticket: str) -> int:
    return int(ticket, 2)


def ticket_to_bin(ticket: str) -> str:
    return ticket.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')


if __name__ == '__main__':
    data = read_file_by_line('input.txt')
    highest = 0
    for ticket in data:
        temp = bin_str_to_int(ticket_to_bin(ticket))
        highest = temp if temp > highest else highest
    print(highest)
