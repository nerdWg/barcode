from main import generate_ean13_code


def test_ean13_code_for_():
    expected = "101 0011001 0010011 0111101 0100011 01010 1100110 1101100 1000010 1001000 101"
    assert generate_ean13_code("12341238") == expected
