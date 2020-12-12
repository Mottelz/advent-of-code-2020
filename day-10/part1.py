from utils import read_file_as_ints
from typing import List


def get_jolt_counts(adapter_list: List[int]) -> (int, int, int):
    one_jolt = 0
    two_jolt = 0
    three_jolt = 0

    for i in range(len(adapter_list) - 1):
        jump = adapter_list[i+1] - adapter_list[i]
        if jump == 1:
            one_jolt += 1
        elif jump == 2:
            two_jolt += 2
        elif jump == 3:
            three_jolt += 1

    return one_jolt, two_jolt, three_jolt


def main():
    data = read_file_as_ints('input.txt')
    data.append(0)
    data.append(max(data) + 3)
    data = sorted(data)
    j1, j2, j3 = get_jolt_counts(data)
    print(f"Part 1: {j1 * j3}, j1: {j1}, j2:{j2}, j3: {j3}")


if __name__ == "__main__":
    main()
