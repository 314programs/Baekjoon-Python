ItemCount = int(input())
SortingList = []

#Append items into the sorting list, word, length of the word and the sum of numbers in the word
for i in range(ItemCount):
  Word = input()
  NumberCount = 0
  for char in Word:
#Used to check if the character is a number
    if char.isdigit():
      NumberCount += int(char)
  SortingList.append([Word, len(Word), NumberCount])

#Use lambda function to sort the list and print
SortingList.sort(key=lambda x:(x[1], x[2], x[0]))
for i in range(ItemCount):
  print(SortingList[i][0])
