import ddt
from src.Multiplication_table import multiplication_table
import unittest


@ddt.ddt
class MultiplicationTableTests(unittest.TestCase):
    def test_multiplication_table(self):
        self.assertEqual(multiplication_table(1, 1), 1)

    @ddt.data(
        (5, 5, 14),
        (128, 128, 4695),
        (1000, 1000, 248083),
    )
    @ddt.unpack
    def test_different_cases(self, num1, num2, expected):
        """Multiplication_table from {} and {} is {}"""
        result = multiplication_table(num1, num2)
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            multiplication_table(-1, -1)

    def test_invalid_input_str(self):
        with self.assertRaises(TypeError):
            multiplication_table('a')


if __name__ == '__main__':
    unittest.main()
