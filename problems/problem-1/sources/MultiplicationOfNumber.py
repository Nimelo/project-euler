from ArithmeticProgression import ArithmeticProgression


class MultiplicationOfNumber:
    """
    Interprets a series number multiplications.
    """
    def __init__(self, n):
        """Constructor

        :param n: The number.
        """
        self.number = n

    def sum_of_elements_smaller_than(self, n):
        """Sums series of an elements which are smaller than a given parameter.

        :param n: Upper boundary (exclusive).
        :return: Sum.
        """
        ap = ArithmeticProgression(self.number, self.number)
        return ap.sum(self._count_of_smaller_than(n))

    def _count_of_smaller_than(self, n):
        """Counts how many numbers is smaller than a given parameter.

        :param n: Upper boundary (exclusive).
        :return: Number of elements.
        """
        if n % self.number == 0:
            return int(n / self.number) - 1
        else:
            return int(n / self.number)
