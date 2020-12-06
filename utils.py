# This file stores the general utility functions.
from typing import List


def read_file_by_line(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def read_file_by_group(filename: str) -> List[str]:
    with open(filename) as file:
        data = file.read().replace('\n\n', '&&&').replace('\n', ' ').split('&&&')
    return data

