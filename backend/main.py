import os

import svgwrite
from svgwrite import Drawing

CENTER_MARKER = '01010'

START_END_MARKER = '101'


def create_ean13_image_xml(number: str) -> str:
    return create_ean13_image(number).tostring()


def create_ean13_image(number: str) -> Drawing:
    code = create_ean13_code(number).replace(" ", "")
    svg = create_image(code)
    return svg


def create_ean13_code(number: str) -> str:
    if len(number) != 12:
        raise Exception("Number must be 12 digits long")
    number_with_check_digit = create_number_with_check_digit(number)
    return _generate_ean13_code(number_with_check_digit)


def create_ean8_image_xml(number: str) -> str:
    return create_ean8_image(number).tostring()


def create_ean8_image(number: str) -> Drawing:
    code = create_ean8_code(number).replace(" ", "")
    return create_image(code)


def create_ean8_code(number: str):
    if len(number) != 7:
        raise Exception("Number must be 7 digits long")
    number_with_check_digit = create_number_with_check_digit(number)
    return _generate_ean8_code(number_with_check_digit)


def create_image(code: str) -> Drawing:
    stroke_width = 5
    margin = 100
    image_width = len(code) * stroke_width + 2 * margin
    image_height = 500
    drawing = svgwrite.Drawing(
        size=(image_width, image_height),
        viewBox=f'0 0 {image_width} {image_height}'
    )
    foreground = 'black'
    background = 'white'
    shapes = drawing.add(drawing.g(id='shapes', fill=background))
    shapes.add(drawing.rect(insert=(0, 0), size=(image_width, image_height)))

    current_offset = margin
    for bit, run_length in runs(code):
        bar_width = stroke_width * run_length
        if bit == '1':
            shapes.add(drawing.rect(
                insert=(current_offset, margin),
                size=(bar_width, image_height - 2 * margin),
                fill=foreground
            ))
        current_offset += bar_width
    return drawing


def runs(code: str):
    current_runs = [[code[0], 1]]
    for bit in code[1:]:
        if bit == current_runs[-1][0]:
            current_runs[-1][1] += 1
        else:
            current_runs.append([bit, 1])
    return current_runs


def create_number_with_check_digit(number: str):
    return number + calc_check_digit(number)


def calc_check_digit(digits: str) -> str:
    odds_sum = sum_digits(digits[-1::-2])
    evens_sum = sum_digits(digits[-2::-2])
    return str((10 - ((odds_sum * 3 + evens_sum) % 10)) % 10)


def sum_digits(digits: str) -> int:
    return sum(map(int, digits))


def l_code_digit(digit: str) -> str:
    l_codes = {
        "0": "0001101",
        "1": "0011001",
        "2": "0010011",
        "3": "0111101",
        "4": "0100011",
        "5": "0110001",
        "6": "0101111",
        "7": "0111011",
        "8": "0110111",
        "9": "0001011"
    }
    return l_codes[digit]


def r_code_digit(digit: str) -> str:
    l_code = l_code_digit(digit)
    return "".join(["0" if bit == "1" else "1" for bit in l_code])


def g_code_digit(digit: str) -> str:
    r_code = r_code_digit(digit)
    return r_code[::-1]


def _generate_ean8_code(number: str):
    return ' '.join([
        START_END_MARKER,
        l_code_digit(number[0]),
        l_code_digit(number[1]),
        l_code_digit(number[2]),
        l_code_digit(number[3]),
        CENTER_MARKER,
        r_code_digit(number[4]),
        r_code_digit(number[5]),
        r_code_digit(number[6]),
        r_code_digit(number[7]),
        START_END_MARKER
    ])


def _generate_ean13_code(number: str):
    ean13_list = [
        START_END_MARKER,
        *encode_first_group(number),
        CENTER_MARKER,
        *encode_last_group(number[7:]),
        START_END_MARKER
    ]

    return ' '.join(ean13_list)


def encode_last_group(number):
    return [r_code_digit(digit) for digit in number]


def encode_first_group(number):
    ean13_structure = {
        "0": "LLLLLL",
        "1": "LLGLGG",
        "2": "LLGGLG",
        "3": "LLGGGL",
        "4": "LGLLGG",
        "5": "LGGLLG",
        "6": "LGGGLL",
        "7": "LGLGLG",
        "8": "LGLGGL",
        "9": "LGGLGL"
    }
    groupings = ean13_structure[number[0]]
    left_list = []
    for digit, encoding in zip(number[1:7], groupings):
        if encoding == "L":
            left_list.append(l_code_digit(digit))
        else:
            left_list.append(g_code_digit(digit))
    return left_list


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    create_ean13_image('202111061500').saveas('output/barcode_ean13.svg')
    create_ean8_image('1040788').saveas('output/barcode_ean8.svg')