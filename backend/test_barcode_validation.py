from ean import is_valid_barcode


def test_valid_ean8_barcode():
    assert is_valid_barcode("40170725")


def test_invalid_ean8_barcode():
    assert not is_valid_barcode("40170729")


def test_valid_ean13_barcode():
    assert is_valid_barcode("0793573679000")


def test_invalid_ean13_barcode():
    assert not is_valid_barcode("0793573679009")
