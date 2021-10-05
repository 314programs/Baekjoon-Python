while True:
  try:
#If the first part of the string is equal to a character in t, it will move on to next character
    s, t = map(str, input().split())
    i = 0
    for char in t:
      if char == s[i]:
        i += 1
      if i == len(s):
        print('Yes')
        break
    if i != len(s):
      print('No')
#Use EOF to end the code
  except:
    break
