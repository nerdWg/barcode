import barcode
from code128 import generate_code128_code
from code39 import generate_code39_code
from ean import generate_ean13_code, generate_ean8_code

CODE_FUNCTIONS = {
    'ean8': generate_ean8_code,
    'ean13': generate_ean13_code,
    'code39': generate_code39_code,
    'code128': generate_code128_code,
}


def get_available_barcode_types() -> [str]:
    return list(CODE_FUNCTIONS.keys())


def create_svg_xml(number: str, type: str) -> str:
    code = create_code(number, type)
    return barcode.create_image_xml(code.replace(" ", ""))


def create_code(number: str, type: str) -> str:
    return CODE_FUNCTIONS[type](number)
