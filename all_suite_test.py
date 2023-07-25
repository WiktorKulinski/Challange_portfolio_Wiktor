import unittest
from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLoginSystem
from test_cases.log_out import TestLogOut
from test_cases.login_with_invalid_password import TestLoginWithInvalidPassword
from test_cases.change_language import TestChangeLanguage

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginSystem))
   test_suite.addTest(makeSuite(TestLoginWithInvalidPassword))
   test_suite.addTest(makeSuite(TestLogOut))
   test_suite.addTest(makeSuite(TestChangeLanguage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
