
import unittest

from tests.question_tests import question_tests_c

suite = unittest.TestLoader().loadTestsFromModule(question_tests_c)
unittest.TextTestRunner(verbosity=2).run(suite)