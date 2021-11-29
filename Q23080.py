s = int(input())
word = input()
w = 0
Result = ''
while w < len(word):
    Result += word[w]
    w += s
print(Result)
