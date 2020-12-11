import re


def parse_data(filename: str) -> dict:
    with open(filename) as file:
        rules = dict()
        for line in file.readlines():
            data = line.replace('\n', '').split(" contain ")
            if data[1] != "no other":
                cleaned = re.split(r"[ ](?=[1-9]\s[a-z]*\s[a-z]*)", data[1])
                done = []
                for s in cleaned:
                    done.append(re.sub(r"[0-9] ", r"", s))
                rules.update({data[0]: done})
            else:
                rules.update({data[0]: None})
        return rules


def get_bag_count(target_bag: str, rules: dict) -> int:
    count = 0
    for rule in rules:
        if rule is target_bag:
            continue
        elif follow_bag_tree(target_bag, rules, rule):
            count += 1
    return count


def follow_bag_tree(target_bag: str, rules: dict, current_rule: str) -> bool:
    print(f"{current_rule}: {rules[current_rule]}")
    # Base Case
    if rules[current_rule] is None:
        return False
    elif target_bag in rules[current_rule]:
        return True
    else:
        final = False
        for rule in rules[current_rule]:
            final = final or follow_bag_tree(target_bag, rules, rule)
        return final


def main():
    rules = parse_data("test.txt")
    count = get_bag_count("shiny gold", rules)
    print(count)


if __name__ == "__main__":
    main()
