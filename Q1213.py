#Count each character in the word
Word = input()
CharDict = {}
for char in Word:
  if char in CharDict:
    CharDict[char] += 1
  else:
    CharDict[char] = 1

CharList = sorted(CharDict.items())

OddCount = 0
Sorry = False

#Check to see if there is 2 or more characters with count of odd number. If there is, the phase cannout be a pelindrome.
for item in CharList:
  if item[1]%2 != 0:
    OddCount += 1
  
  if OddCount == 2:
    Sorry = True
    break

if Sorry:
  print("I'm Sorry Hansoo")
#Make a pelindrome by rearranging the word, it will be alphabetically forward as well, since the dictionary was sorted.
else:
  Front = ''
  Mid = ''
  for item in CharList:
    if item[1]%2 != 0:
      Front += item[0] * (item[1]//2)
      Mid = item[0]
    else:
      Front += item[0] * (item[1]//2)
  print(Front + Mid + Front[::-1])
