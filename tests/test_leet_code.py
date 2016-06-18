import unittest
from leet_code.count_numbers_with_unique_digits import *


class LeetCodeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @execution_timer()
    def test_count_numbers_with_unique_digits_combinatorics_1bit(self):
        result = count_numbers_with_unique_digits_combinatorics(1)

        self.assertEqual(result, 10)

    @execution_timer()
    def test_count_numbers_with_unique_digits_combinatorics_2bit(self):
        result = count_numbers_with_unique_digits_combinatorics(2)

        self.assertEqual(result, 91)

    def test_count_numbers_with_unique_digits_backtracking_1bit(self):
        result = count_numbers_with_unique_digits_backtracking(1)

        self.assertEqual(result, 9)

    def test_count_numbers_with_unique_digits_backtracking(self):
        result = count_numbers_with_unique_digits_backtracking(5)

        self.assertEqual(result, 32491)

