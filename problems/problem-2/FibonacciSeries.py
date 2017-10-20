from itertools import takewhile


def fibonacci_series():
    last = 1
    current = 1

    yield last
    while True:
        tmp = current
        current += last
        last = tmp
        yield current


if __name__ == "__main__":
    smaller_than_4_millions = takewhile(lambda x: x < 4e6 + 1, fibonacci_series())
    even_numbers = filter(lambda x: x % 2 == 0, smaller_than_4_millions)
    sum = sum(list(even_numbers))
    print(f"The result is {sum}")
