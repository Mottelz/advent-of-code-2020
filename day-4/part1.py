from typing import List
# REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def read_and_clean_data() -> List[str]:
    with open('input.txt') as file:
        data = file.read().replace('\n\n', '&&&').replace('\n', ' ').split('&&&')
    return data


def validate_all_passports(passports: List[str]) -> int:
    number_of_valid = 0
    for passport in passports:
        number_of_valid = number_of_valid + 1 if validate_passport_v1(passport) else number_of_valid
    return number_of_valid


def validate_passport_v1(passport: str) -> bool:
    for field in REQUIRED_FIELDS:
        if field not in passport:
            return False
    return True


if __name__ == '__main__':
    passports = read_and_clean_data()
    print((validate_all_passports(passports)))
