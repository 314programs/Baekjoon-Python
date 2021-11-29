a, b = map(int, input().split())
Result = 0
for c in str(a):
    for d in str(b):
        Result += int(c)*int(d)
print(Result)
