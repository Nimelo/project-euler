from itertools import takewhile


def fibonacci_series():
    last, current = 0, 1

    while True:
        current, last = current + last, current
        yield current


def even_fibonacci_series():
    last, current = 0, 1

    while True:
        current, last = current + last, current
        current, last = current + last, current
        current, last = current + last, current
        yield last


if __name__ == "__main__":
    n = 4e6
    smaller_than_4_millions = takewhile(lambda x: x < n + 1, fibonacci_series())
    even_numbers = filter(lambda x: x % 2 == 0, smaller_than_4_millions)
    result = sum(list(even_numbers))
    print(f"The result is {result}")

    smaller_than_4_millions = takewhile(lambda x: x < n + 1, even_fibonacci_series())
    result = sum(list(smaller_than_4_millions))

    print(f"The result is {result}")
