from palindrome import pal


def testPositivePalindrome():
  assert pal('radar')

def testNegativePalindrome():
  assert pal('dog') == False

def testPalindromeNumbers():
  assert pal('11211')

def testPalindromeFalseNumbers():
  assert pal('123') == False