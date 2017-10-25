from math import log, sqrt


def lower_bound(n):
    return n * log(n) + n * (log(log(n)) - 1)


def upper_bound(n):
    return n * log(n) + n * log(log(n))


def naive_is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    if n in [2, 3, 5, 7]:
        return True
    if n % 3 == 0:
        return False
    """
    The check is made for odd integers not divisible by 3
    6k +/- {1, 5}
    """
    ub, i, j = int(sqrt(n)), 5, 7
    while i <= ub or j <= ub:
        if n % i == 0:
            return False
        if n % j == 0:
            return False
        i, j = i + 6, j + 6
    return True


def nth_prime(n):
    primes, i = 1, 1
    while primes < n:
        i += 2
        if is_prime(i):
            primes += 1
    return i


def naive_nth_prime(n):
    primes, index = 1, 1
    while primes < n:
        index += 2
        if naive_is_prime(index):
            primes += 1
    return index


if __name__ == "__main__":
    n = 10001
    print(f"Lower bound {lower_bound(n)}")
    print(f"Upper bound {upper_bound(n)}")
    print(nth_prime(n))
    print(naive_nth_prime(n))
