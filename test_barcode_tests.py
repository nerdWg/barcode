from main import calc_check_digit


def test_0000000_yields_0():
    number = '0000000'
    assert (calc_check_digit(number) == '0')


def test_4017072_yields_5():
    number = '4017072'
    assert (calc_check_digit(number) == '5')


def test_7124512_yields_6():
    number = '7124512'
    assert (calc_check_digit(number) == '6')


def test_4229639_yields_3():
    number = '4229639'
    assert (calc_check_digit(number) == '3')


def test_0303040_yields_0():
    number = '0303040'
    assert (calc_check_digit(number) == '0')


def test_0102070_yields_0():
    number = '0102070'
    assert (calc_check_digit(number) == '0')


def test_1212141_yields_0():
    number = '1212141'
    assert (calc_check_digit(number) == '0')


def test_079357367900_yields_0():
    number = '079357367900'
    assert (calc_check_digit(number) == '0')
