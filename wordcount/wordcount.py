def wc(str):
  i = 1 

  for c in str:
    if c == ' ':
      i += 1

  return i

if __name__ == '__main__':
  inp = input('Please enter a string: ')
  print('There are ' + str(wc(inp)) + ' words.')