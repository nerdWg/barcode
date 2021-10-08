def calc_check_digit(digits: str) -> int:
    odds_sum = sum_digits(digits[-1::-2])
    evens_sum = sum_digits(digits[-2::-2])
    return (10 - ((odds_sum * 3 + evens_sum) % 10)) % 10


def sum_digits(digits: str) -> int:
    return sum(map(int, digits))


def l_code_digit(digit: str) -> str:
    l_codes = {"0": "0001101"}
    return l_codes[digit]


def r_code_digit(digit: str) -> str:
    l_code = l_code_digit(digit)
    return "".join(["0" if bit == "1" else "1" for bit in l_code])


def g_code_digit(digit: str) -> str:
    r_code = r_code_digit(digit)
    return r_code[::-1]
