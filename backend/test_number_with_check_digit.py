from main import create_number_with_check_digit


def test_ean8():
    assert create_number_with_check_digit("7124512") == "71245126"


def test_ean13():
    assert create_number_with_check_digit("079357367900") == "0793573679000"
