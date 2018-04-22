import unittest
from Lecture3.homework.task6 import is_year_leap


class TestLeafYear(unittest.TestCase):

    def test_2000_year(self):
        self.assertTrue(is_year_leap(2000))

    def test_1996_year(self):
        self.assertTrue(is_year_leap(1996))

    def test_1993_year(self):
        self.assertFalse(is_year_leap(1993))

    def test_string_values(self):
        self.assertEqual('string values are not accepted!', is_year_leap('text'))

    def test_0_year(self):
        self.assertEqual('Wrong year', is_year_leap(0))


if __name__ == '__main__':
    unittest.main()