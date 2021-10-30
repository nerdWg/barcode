from main import l_code_digit, r_code_digit, g_code_digit


def test_0_yields_0001101():
    assert (l_code_digit("0")) == "0001101"


def test_r_code_0_1110010():
    assert (r_code_digit("0")) == "1110010"


def test_g_code_0_0100111():
    assert (g_code_digit("0")) == "0100111"
