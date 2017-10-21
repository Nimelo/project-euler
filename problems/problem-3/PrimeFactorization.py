from math import sqrt


def prime_factorization(n):
    factors = [1, 2] if n % 2 == 0 else [1]
    n, factor = n, 3
    max_factor = int(sqrt(n))
    while n != 1 and factor <= max_factor:
        if n % factor == 0:
            factors.append(factor)
            while n % factor == 0:
                n = n // factor
            max_factor = int(sqrt(n))
        factor = factor + 2
    if n != 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    n = 600851475143
    print(prime_factorization(n))
