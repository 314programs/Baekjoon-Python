#Need to practice for USACO, not this year but maybe this eyar
a, b = map(int, input().split())
c, d = map(int, input().split())

TheList = [0]*101
for i in range(a, b):
    TheList[i] = 1
for i in range(c, d):
    TheList[i] = 1

print(TheList.count(1))
