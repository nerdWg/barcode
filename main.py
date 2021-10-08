def calc_check_digit(digits: str) -> int:
    odds_sum = sum_digits(digits[-1::-2])
    evens_sum = sum_digits(digits[-2::-2])
    return (10 - ((odds_sum * 3 + evens_sum) % 10)) % 10


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
