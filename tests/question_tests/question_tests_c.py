#test 3

import unittest

from src.question_c.question_c import use_global

global_var = 0

class Test_Config(unittest.TestCase):

    def test_use_global(self):

        global global_var
        self.assertEqual(True, global_var == 0)
        self.assertEqual(False, use_global() == 0)