from MultiplicationOfNumber import MultiplicationOfNumber

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
if __name__ == "__main__":
    n = 1000
    sumOfThree = MultiplicationOfNumber(3).sum_of_elements_smaller_than(n)
    sumOfFive = MultiplicationOfNumber(5).sum_of_elements_smaller_than(n)
    sumOfFifteen = MultiplicationOfNumber(15).sum_of_elements_smaller_than(n)

    result = sumOfThree + sumOfFive - sumOfFifteen

    print(f"The result is {result}")
