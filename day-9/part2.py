from typing import List
EXPLOIT_VALUE = 25918798  # Value comes from part one


def parse_file(filename: str) -> List[int]:
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(eval(line))
    return data


def get_key(msg: List[int]) -> int:
    for start in range(len(msg) - 1):
        for end in range(start+1, len(msg)):
            msg_segment = msg[start:end+1]
            value_to_check = sum(msg_segment)
            if value_to_check == EXPLOIT_VALUE:
                return min(msg_segment) + max(msg_segment)
            elif value_to_check > EXPLOIT_VALUE:
                break


def main():
    msg = parse_file('input.txt')
    part2 = get_key(msg)
    print(part2)


if __name__ == "__main__":
    main()