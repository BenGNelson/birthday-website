import unittest
import datetime

class TestSum(unittest.TestCase):

    def test_month(self):
        date = datetime.datetime(2021, 1, 1)
        self.assertEqual(date.month, 1, "Should be 1")

    def test_day(self):
        date = datetime.datetime(2021, 3, 4)
        self.assertEqual(date.day, 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()