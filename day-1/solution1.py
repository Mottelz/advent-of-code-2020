from typing import List
YEAR = 2020


# Part 1 solution
def part1(numbers: List[int]):
    for n1 in range(0, len(numbers)):
        for n2 in range(n1+1, len(numbers)):
            if numbers[n1] + numbers[n2] == YEAR:
                print(f"n1: {numbers[n1]}, n2: {numbers[n2]}, sum: {numbers[n1]+numbers[n2]}, product: {numbers[n1]*numbers[n2]}")
                break


# Part 2 Solution
def part2(numbers: List[int]):
    for n1 in range(0, len(numbers)):
        for n2 in range(n1+1, len(numbers)):
            for n3 in range(n2+1, len(numbers)):
                if numbers[n1] + numbers[n2] + numbers[n3] == YEAR:
                    print(f"n1: {numbers[n1]}, n2: {numbers[n2]}, n3: {numbers[n3]} sum: {numbers[n1]+numbers[n2]+numbers[n3]}, product: {numbers[n1]*numbers[n2]*numbers[n3]}")
                    break


# Main
def main():
    # Read in file
    with open('input.txt', 'r') as file:
        data = file.read().split()

    # Convert to numbers and remove bigger than year
    numbers = [eval(num) for num in data if eval(num) < YEAR]
    part1(numbers)
    part2(numbers)


# Run main
main()
