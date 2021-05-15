def pal(str):
  strReverse = str[::-1]
  return str == strReverse


if __name__ == "__main__":
  str = input('Please input a string: ')
  isPalindrome = pal(str)
  if isPalindrome:
    print('The string is a palindrome')
  else:
    print('The string is not a palindrome')