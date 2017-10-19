import unittest
from MultiplicationOfNumber import MultiplicationOfNumber


class MultiplicationOfNumberTest(unittest.TestCase):

    def test_sum_of_3(self):
        n = 10
        mn = MultiplicationOfNumber(3)
        sum = mn.sum_of_elements_smaller_than(n)
        self.assertEqual(18, sum)

    def test_sum_of_5(self):
        n = 10
        mn = MultiplicationOfNumber(5)
        sum = mn.sum_of_elements_smaller_than(n)
        self.assertEqual(5, sum)

    def test_count_of_3(self):
        n = 10
        mn = MultiplicationOfNumber(3)
        count = mn._count_of_smaller_than(n)
        self.assertEqual(3, count)

    def test_count_of_5(self):
        n = 10
        mn = MultiplicationOfNumber(5)
        count = mn._count_of_smaller_than(n)
        self.assertEqual(1, count)
