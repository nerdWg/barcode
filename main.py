def calc_check_digit(digits: str) -> int:
    odds_sum = sum_digits(digits[-1::-2])
    evens_sum = sum_digits(digits[-2::-2])
    return (10 - ((odds_sum * 3 + evens_sum) % 10)) % 10


def sum_digits(digits: str) -> int:
    return sum(map(int, digits))
