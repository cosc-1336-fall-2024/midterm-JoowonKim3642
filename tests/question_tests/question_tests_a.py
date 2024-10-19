#test 1

import unittest

from src.question_a.question_a import get_random_number 

class Test_Config(unittest.TestCase):

    def test_get_random_number(self):
        num = get_random_number()
        self.assertEqual(True, num<=5 and num>=1 )