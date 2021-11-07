import barcode
from code39 import generate_code39_code
from ean import generate_ean13_code, generate_ean8_code


def create_image_xml(number: str, type: str) -> str:
    code = create_code(number, type)
    return barcode.create_image_xml(code.replace(" ", ""))


def create_code(number: str, type: str) -> str:
    if type.startswith('ean'):
        number = create_number_with_check_digit(number)
    return {
        'ean8': generate_ean8_code,
        'ean13': generate_ean13_code,
        'code39': generate_code39_code
    }[type](number)


def create_number_with_check_digit(number: str):
    return number + calc_check_digit(number)


def calc_check_digit(digits: str) -> str:
    odds_sum = sum_digits(digits[-1::-2])
    evens_sum = sum_digits(digits[-2::-2])
    return str((10 - ((odds_sum * 3 + evens_sum) % 10)) % 10)


def sum_digits(digits: str) -> int:
    return sum(map(int, digits))


def is_valid_barcode(barcode: str) -> bool:
    return calc_check_digit(barcode[:-1]) == barcode[-1]
