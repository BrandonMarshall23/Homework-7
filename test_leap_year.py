import leap_year
import unittest
class TestLeapYear(unittest.TestCase):
    def div_by_4(self):
       self.assertEqual(leap_year.process, True)
if __name__ == '__main__':
    unittest.main()