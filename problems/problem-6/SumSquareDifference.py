def sum_square_difference(n):
    first_term = n * (n + 1)
    second_term = 3 * n ** 2 - n - 2
    return first_term * second_term / 12


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


def square_of_sum(n):
    return (0.5 * n * (n + 1)) ** 2


if __name__ == "__main__":
    print(sum_square_difference(10))
    print(sum_square_difference(100))
    print(square_of_sum(10) - sum_of_squares(10))
    print(square_of_sum(100) - sum_of_squares(100))
