from typing import List


def parse_file(filename: str) -> List[int]:
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(eval(line))
    return data


def find_exploit(msg: List[int], offset: int = 25) -> int:
    for i in range(offset, len(msg)):
        if not validate_number(msg[i], msg[:i]):
            return msg[i]


def validate_number(num_to_check, check_against):
    for num in check_against:
        if num_to_check - num in check_against:
            return True
    return False


def main():
    msg = parse_file('input.txt')
    part1 = find_exploit(msg)
    print(part1)


if __name__ == "__main__":
    main()