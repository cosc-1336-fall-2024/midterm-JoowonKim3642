
import unittest

from tests.question_tests import question_tests_d

suite = unittest.TestLoader().loadTestsFromModule(question_tests_d)
unittest.TextTestRunner(verbosity=2).run(suite)