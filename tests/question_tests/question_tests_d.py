#test 4

import unittest

from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_get_day_of_week(self):
        self.assertEqual("Invalid number", get_day_of_week(0))
        self.assertEqual("Monday", get_day_of_week(1))
        self.assertEqual("Tuesday", get_day_of_week(2))
        self.assertEqual("Wednesday", get_day_of_week(3))
        self.assertEqual("Invalid number", get_day_of_week(8))