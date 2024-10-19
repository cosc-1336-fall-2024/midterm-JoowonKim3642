#test 3

import unittest

from src.question_c.question_c import use_global

class Test_Config(unittest.TestCase):
    
    global_var = 0

    def test_get_random_number(self):
        global global_var
        self.assertEqual(True, global_var == 0)
        use_global()
        self.assertEqual(False, global_var == 0 )