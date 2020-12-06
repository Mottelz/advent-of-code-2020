from utils import read_file_by_group


def get_group_agreement(group: str) -> int:
    individual_answers = group.split(' ')
    final_strings = individual_answers[0]
    for i in range(1, len(individual_answers)):
        final_strings = string_intersection(final_strings, individual_answers[i])
    return len(final_strings)


def string_intersection(s1: str, s2: str) -> str:
    out = ''
    for letter in s1:
        if letter in s2 and letter not in out:
            out += letter
    return out


def main():
    groups_data = read_file_by_group('input.txt')
    total = 0
    for group in groups_data:
        total += get_group_agreement(group)
    print(total)


if __name__ == '__main__':
    main()
