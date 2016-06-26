import unittest
from leet_code.count_numbers_with_unique_digits import *
from leet_code.int_to_english import *
from leet_code.reverse_string import *
from leet_code.valid_number import *

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


    def test_int_to_english_recursive(self):
        result = int_to_english_recursive(3)
        self.assertEqual(result, "Three")

        result = int_to_english_recursive(123)
        self.assertEqual(result, "One Hundred Twenty Three")

        result = int_to_english_recursive(12345)
        self.assertEqual(result, "Twelve Thousand Three Hundred Forty Five")

        result = int_to_english_recursive(1234567)
        self.assertEqual(result, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")


    def test_reverse_string_pythonic(self):
        input_str = "hello"
        result = reverse_string_pythonic(input_str)

        self.assertEqual("olleh", result)

    def test_reverse_string(self):
        input_str = "hello"
        result = reverse_string(input_str)

        self.assertEqual("olleh", result)

    def test_is_validate_num(self):
        self.assertTrue(is_validate_num("0"))
        self.assertTrue(is_validate_num("0.1"))
        self.assertTrue(is_validate_num("-1"))
        self.assertTrue(is_validate_num("2e10"))
        self.assertTrue(is_validate_num(".8"))
        self.assertTrue(is_validate_num(".1 "))

        self.assertFalse(is_validate_num("1a"))
        self.assertFalse(is_validate_num("abc"))
        self.assertFalse(is_validate_num("0e"))
