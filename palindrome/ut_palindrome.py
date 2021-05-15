import unittest
from palindrome import pal


class test_palindrome(unittest.TestCase):
  def testPositivePalindrome(self):
    self.assertTrue(pal('radar'))

  def testNegativePalindrome(self):
    self.assertFalse(pal('dog'))

  def testPalindromeNumbers(self):
    self.assertTrue(pal('1112111'))

  def testPalindromeFalseNumbers(self):
    self.assertFalse(pal('123'))


if __name__ == '__main__':
  unittest.main()