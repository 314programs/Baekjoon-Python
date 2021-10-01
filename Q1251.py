word = input()
wordsList = []
#Find all possible words available
for a in range(1, len(word)-1):
  for b in range(2,len(word)):
#Since when it is set to a!= b, it can repeat outcomes we will go with a<b
    if a < b:
      wordsList.append(word[0:a][::-1] + word[a:b][::-1] + word[b:len(word)][::-1])
wordsList.sort()
print(wordsList[0])
