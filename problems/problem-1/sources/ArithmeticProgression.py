class ArithmeticProgression:
    """
    Class which stores information about the arithmetic progression.
    """
    def __init__(self, a, d):
        """Constructor

        :param a: First element.
        :param d: Difference between two successive members of a progression.
        """
        self.a = a
        self.d = d

    def sum(self, n):
        """Returns the sum of n first elements of arithmetic progression.

        :param n: Elements of arithmetic progression.
        :return: Sum of arithmetic progression
        """
        nth = self._get_nth_element(n)
        return 0.5 * n * (self.a + nth)

    def _get_nth_element(self, n):
        """Returns the n-th element of an arithmetic progression.

        :param n: Index of an element.
        :return: N-th element of an arithmetic progression.
        """
        return self.a + (n - 1) * self.d
