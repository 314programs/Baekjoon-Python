Needed = int(input())
TimeList = [300, 60, 10]
Result = [0,0,0]
for i in range(3):
    item = TimeList[i]
    if item <= Needed:
        Result[i] += Needed//item
        Needed -= item*(Needed//item)

if Needed == 0:
    print(' '.join(map(str, Result)))
else:
    print(-1)
