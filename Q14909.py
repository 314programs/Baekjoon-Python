TheList = map(int, input().split())
Count = 0
for item in TheList:
    if item > 0:
        Count += 1
print(Count)
