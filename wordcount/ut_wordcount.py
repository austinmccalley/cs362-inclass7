import unittest
from wordcount import wc

class test_wordcount(unittest.TestCase):
  def testSentence(self):
    self.assertEqual(wc('This is an activity.'), 4)

  def testTwoSentences(self):
    self.assertEqual(wc('Hey! This word count is pretty cool!'), 7)

  def testOneSentenceFalse(self):
    self.assertNotEqual(wc('This is an activity'), 6)

  def testOneWordFalse(self):
    self.assertNotEqual(wc('Hey'), 2)

if __name__ == '__main__':
  unittest.main()
