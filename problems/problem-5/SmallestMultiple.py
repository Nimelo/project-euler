from functools import reduce


def lcma(args):
    return reduce(lcm, args)


def lcm(a, b):
    nominator = a * b
    denominator = gcd(a, b)
    return nominator / denominator


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    print(lcma(range(1, 20 + 1)))