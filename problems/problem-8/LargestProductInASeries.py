from StaticData import get_1000_digit_number
from functools import reduce


def multiply_digits(string):
    digits = [int(x) for x in string]
    return reduce(lambda x, y: x * y, digits)


def generate_sub_sequences(string, length):
    for i in range(0, len(string) - length + 1):
        yield string[i: i + length]


def find_greatest_product(string, length):
    return max(list({multiply_digits(s) for s in generate_sub_sequences(string, length)}))


if __name__ == "__main__":
    n = get_1000_digit_number()
    print(find_greatest_product(n, 4))
    print(find_greatest_product(n, 13))
