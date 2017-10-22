def is_palindrome(string):
    for i, char in enumerate(string[:len(string) // 2]):
        if char != string[-i - 1]:
            return False
    return True


def find_all_palindromes():
    palindromes = []
    for i in range(999, 99, -1):
        for j in range(999, i, -1):
            multiplication = i * j
            if is_palindrome(str(multiplication)):
                palindromes.append(multiplication)
    return palindromes


def find_max_palindrome():
    upper, largest_palindrome = 999, 0
    while upper >= 100:
        lower, delta_lower = (999, 1) if upper % 11 == 0 else (990, 11)
        while lower >= upper:
            palindrome = upper * lower
            if palindrome <= largest_palindrome:
                break
            if is_palindrome(str(palindrome)):
                largest_palindrome = palindrome
            lower -= delta_lower
        upper -= 1
    return largest_palindrome


if __name__ == "__main__":
    print(max(find_all_palindromes()))
    print(find_max_palindrome())
