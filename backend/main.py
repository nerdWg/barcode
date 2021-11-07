import os

import svgwrite
from svgwrite import Drawing

from ean import generate_ean13_code, generate_ean8_code


def create_ean13_image_xml(number: str) -> str:
    return create_ean13_image(number).tostring()


def create_ean8_image_xml(number: str) -> str:
    return create_ean8_image(number).tostring()


def create_ean13_image(number: str) -> Drawing:
    code = create_ean13_code(number).replace(" ", "")
    svg = create_image(code)
    return svg


def create_ean8_image(number: str) -> Drawing:
    code = create_ean8_code(number).replace(" ", "")
    return create_image(code)


def create_ean13_code(number: str) -> str:
    if len(number) != 12:
        raise Exception("Number must be 12 digits long")
    number_with_check_digit = create_number_with_check_digit(number)
    return generate_ean13_code(number_with_check_digit)


def create_ean8_code(number: str):
    if len(number) != 7:
        raise Exception("Number must be 7 digits long")
    number_with_check_digit = create_number_with_check_digit(number)
    return generate_ean8_code(number_with_check_digit)


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


def is_valid_barcode(barcode: str) -> bool:
    return calc_check_digit(barcode[:-1]) == barcode[-1]


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    create_ean13_image('202111061500').saveas('output/barcode_ean13.svg')
    create_ean8_image('1040788').saveas('output/barcode_ean8.svg')
