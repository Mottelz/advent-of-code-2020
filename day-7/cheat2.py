# I kinda gave up and stole this answer from https://github.com/sophiebits/adventofcode/blob/main/2020/day07.py
import collections
import re

with open('original.txt') as file:
    lines = file.readlines()

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)
for line in lines:
    color = re.match(r'(.+?) bags contain', line)[1]
    for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        ct = int(ct)
        containedin[innercolor].add(color)
        contains[color].append((ct, innercolor))


def cost(color):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct * cost(inner)
    return total
print(cost('shiny gold'))