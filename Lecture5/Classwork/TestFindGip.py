import unittest
from Lecture3.practice4 import find_gip


class TestFindGip(unittest.TestCase):

    def test_zero(self):
        res = find_gip(9, 5)
        self.assertEqual(res, 10.295630140987)


if __name__ == '__main__':
    unittest.main()