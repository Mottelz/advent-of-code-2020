# This does not work and I have no idea why. I'll possibly come back to it eventually.
import re


def parse_data(filename: str) -> dict:
    with open(filename) as file:
        rules = dict()
        for line in file.readlines():
            data = line.replace('\n', '').split(" contain ")
            if data[1] != "no other":
                cleaned = re.split(r"[ ](?=[1-9]\s[a-z]*\s[a-z]*)", data[1])
                rules.update({data[0]: cleaned})
            else:
                rules.update({data[0]: None})
        return rules


def get_bag_count(target_bag: str, rules: dict) -> int:
    count = 0
    for rule in rules[target_bag]:
        amount, bag = split_bag_and_count(rule)
        count += get_internal_bag_count(rules, bag) * amount
        print(f"count: {count}, bag: {bag}")
    return count


def get_internal_bag_count(rules: dict, current_bag: str) -> int:
    if rules[current_bag] is None:
        return 1
    else:
        sum = 1
        for rule in rules[current_bag]:
            amount, bag = split_bag_and_count(rule)
            print(f"amount: {amount}, bag: {bag}")
            sum += amount * get_internal_bag_count(rules, bag) + 1
        return sum


def split_bag_and_count(raw: str) -> (int, str):
    result = re.split(r"(?<=[1-9])[ ]", raw)
    return eval(result[0]), result[1]


def main():
    rules = parse_data("test2.txt")
    count = get_bag_count("shiny gold", rules)
    print(count)


if __name__ == "__main__":
    main()
