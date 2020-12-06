from utils import read_file_by_group


def main():
    groups_data = read_file_by_group('input.txt')
    total = 0
    for group in groups_data:
        total += len(set(group.replace(' ', '')))
    print(total)


if __name__ == '__main__':
    main()
