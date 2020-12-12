from utils import read_file_as_ints
from typing import List


def walk_backwards(adapter_list: List[int]) -> int:
    paths = {max(adapter_list): 1}
    for i in range(len(adapter_list)-2, -1, -1):
        current = adapter_list[i]
        possible_children = [current+1, current+2, current+3]
        paths[current] = 0
        for n in possible_children:
            try:
                paths[current] += paths[n]
            except Exception:
                pass
    return paths[0]


def main():
    adapter_list = read_file_as_ints('input.txt')
    adapter_list.append(0)
    adapter_list = sorted(adapter_list)
    part2 = walk_backwards(adapter_list)
    print(part2)


if __name__ == "__main__":
    main()
