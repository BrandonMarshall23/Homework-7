import leap_year
import unittest
class TestLeapYear(unittest.TestCase):
    def div_by_4(self):
       self.assertEqual(leap_year.process, True)
    def div_by_100(self):
       self.assertEqual(leap_year.process, True)
    def div_by_400(self):
       self.assertEqual(leap_year.process, True)
    def final_test(self):
        self.assertEqual(leap_year.process(2000),Leap Year)
        self.assertEqual(leap_year.process(1999),False)
        self.assertEqual(leap_year.process(1600),Leap Year)
if __name__ == '__main__':
    unittest.main()
