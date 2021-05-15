from wordcount import wc

def testSentence():
  assert wc('This is an activity') ==  4

def testTwoSentences():
  assert wc('Hey! This word count is pretty cool!') == 7

def testOneSentenceFalse():
  assert wc('This is an activity.') != 6

def testOneWorldFalse():
  assert wc('Hey!') != 2 