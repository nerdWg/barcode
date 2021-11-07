from ean import generate_ean13_code, generate_ean8_code, create_ean8_image, create_ean13_image


def create_image_xml(number: str, type: str) -> str:
    number_with_check_digit = create_number_with_check_digit(number)
    if type == 'ean8':
        return create_ean8_image(number_with_check_digit).tostring()
    elif type == 'ean13':
        return create_ean13_image(number_with_check_digit).tostring()


def create_code(number: str, type: str) -> str:
    number_with_check_digit = create_number_with_check_digit(number)
    if type == 'ean8':
        return generate_ean8_code(number_with_check_digit)
    elif type == 'ean13':
        return generate_ean13_code(number_with_check_digit)


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
