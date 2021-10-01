def calc_check_digit(number: int):

    digits = [i for i in str(number)]
    print(digits)
    odds = digits[-1::-2]
    evens = digits[-2::-2]
    odds_sum = sum([int(i)*3 for i in odds])
    evens_sum = sum([int(i) for i in evens])

    return (10-((odds_sum+evens_sum)%10))%10


if __name__ == '__main__':
    calc_check_digit(1234567)