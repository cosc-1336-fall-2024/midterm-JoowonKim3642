#test 2

import unittest

from src.question_b.question_b import get_sum_of_evens

class Test_Config(unittest.TestCase):

    def test_get_sum_of_evens(self):
        self.assertEqual(30, get_sum_of_evens(11))
        self.assertEqual(30, get_sum_of_evens(10))
        self.assertEqual(20, get_sum_of_evens(8))