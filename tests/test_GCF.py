"""
Оформите задачу 4.7 в виде функции и покройте ее тестами.
Учтите, что в функцию могут быть переданы некорректные значения,
здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила
все возможные ситуации сама.
"""


import ddt
import unittest
from src.GCF import gcf


@ddt.ddt
class GCFTests(unittest.TestCase):
    def test_gcf(self):
        self.assertEqual(gcf(99, 11), 11)

    @ddt.data(
        (30, 18, 6),
        (30, 18, 4),
        (39, 16, 1),
        (44, 16, 4),
        (99, 18, 9),
        (9, 9, 9),
        (0, 0, 0),
    )
    @ddt.unpack
    def test_different_cases(self, num1, num2, expected):
        """GCF from {} and {} is {}"""
        result = gcf(num1, num2)
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            gcf(-10, -1)

    def test_invalid_input_str(self):
        with self.assertRaises(TypeError):
            gcf('a', 'b')


if __name__ == '__main__':
    unittest.main()
