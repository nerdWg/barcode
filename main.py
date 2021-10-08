import svgwrite

CENTER_MARKER = '01010'

START_END_MARKER = '101'


def create_ean8_image(number: str):
    code = generate_ean8_code(number_with_check_digit(number)).replace(" ", "")
    create_image(code)


def create_ean13_image(number: str):
    code = generate_ean13_code(number_with_check_digit(number)).replace(" ", "")
    print(code)
    create_image(code)


def create_image(code: str):
    stroke_width = 0.2
    width = len(code) + 10
    height = 20
    offset_x = 5
    dwg = svgwrite.Drawing('test.svg', size=(width, height))

    shapes = dwg.add(dwg.g(id='shapes', fill='white'))
    # override the 'fill' attribute of the parent group 'shapes'
    shapes.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))

    for i, bit in enumerate(code):
        color = 'white' if bit == '0' else 'black'
        dwg.add(dwg.line((i * stroke_width + offset_x, 5), (i * stroke_width + offset_x, 15), stroke=color, stroke_width=stroke_width * 1.1))
    dwg.save()


def number_with_check_digit(number: str):
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


def generate_ean8_code(number: str):
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


def generate_ean13_code(number: str):
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
    create_ean8_image('9638507')
    # create_ean13_image('871125300120')
