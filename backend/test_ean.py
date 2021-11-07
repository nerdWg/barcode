from main import generate_ean8_code


def test_ean8_code_for_12341238():
    expected = "101 0011001 0010011 0111101 0100011 01010 1100110 1101100 1000010 1001000 101"
    assert generate_ean8_code("1234123") == expected


from ean import l_code_digit, r_code_digit, g_code_digit, generate_ean13_code


def test_0_yields_0001101():
    assert (l_code_digit("0")) == "0001101"


def test_r_code_0_1110010():
    assert (r_code_digit("0")) == "1110010"


def test_g_code_0_0100111():
    assert (g_code_digit("0")) == "0100111"


def test_ean13_code_starting_with_0():
    expected = "101 0011001 0010011 0111101 0100011 0011001 0010011 01010 1100110 1101100 1000010 1100110 1101100 1010000 101"
    assert generate_ean13_code("012341212312") == expected
