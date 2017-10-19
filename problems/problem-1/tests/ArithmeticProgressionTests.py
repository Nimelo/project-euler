import unittest

from ArithmeticProgression import ArithmeticProgression


class ArithmeticProgressionTest(unittest.TestCase):

    def test_get_nth_should_return_2(self):
        expected = 2
        ap = ArithmeticProgression(1, 1)
        actual = ap._get_nth_element(2)
        self.assertEqual(actual, expected)

    def test_get_nth_should_return_10(self):
        expected = 10
        ap = ArithmeticProgression(1, 1)
        actual = ap._get_nth_element(10)
        self.assertEqual(actual, expected)

    def test_simple_sum(self):
        ap = ArithmeticProgression(1, 1)
        self.assertEqual(sum(range(1, 11, 1)), ap.sum(10), "Invalid value")
