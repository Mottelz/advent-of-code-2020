from typing import List

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def read_and_clean_data() -> List[str]:
    with open('input.txt') as file:
        data = file.read().replace('\n\n', '&&&').replace('\n', ' ').split('&&&')
    return data


def str_to_passport_dict(raw: str) -> dict:
    clean = raw.split(' ')
    out = dict([s.split(':', 1) for s in clean])
    return out


def validate_passport_v1(passport: str) -> bool:
    for field in REQUIRED_FIELDS:
        if field not in passport:
            return False
    return True


def validate_passport_v2(passport: dict) -> bool:
    return validate_number(passport['byr'], 1920, 2002) and \
           validate_number(passport['iyr'], 2010, 2020) and \
           validate_number(passport['eyr'], 2020, 2030) and \
           validate_height(passport['hgt']) and \
           validate_eyes(passport['ecl']) and \
           validate_hair(passport['hcl']) and \
           validate_passport_id(passport['pid'])


def validate_number(year: str, min_val: int, max_val: int) -> bool:
    return min_val <= eval(year) <= max_val


def validate_height(height: str) -> bool:
    if 'cm' in height:
        return validate_number(height.replace('cm', ''), 150, 193)
    elif 'in' in height:
        return validate_number(height.replace('in', ''), 59, 76)
    else:
        return False


def validate_eyes(colour: str) -> bool:
    return colour in VALID_EYE_COLORS


def validate_hair(colour: str) -> bool:
    if colour[0] != '#' or len(colour) != 7:
        return False
    colour = colour.replace('#', '')
    for letter in colour:
        if not (ord('0') <= ord(letter) <= ord('9') or ord('a') <= ord(letter) <= ord('f')):
            return False
    return True


def validate_passport_id(pid: str) -> bool:
    if len(pid) != 9:
        return False
    for letter in pid:
        if not (ord('0') <= ord(letter) <= ord('9')):
            return False
    return True


if __name__ == '__main__':
    raw = read_and_clean_data()
    count = 0
    old = 0
    for pass_str in raw:
        if validate_passport_v1(pass_str):
            count = count + 1 if validate_passport_v2(str_to_passport_dict(pass_str)) else count
    print(f"valid passports: {count}")
