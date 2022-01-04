#Another USACO for the day...
casecount = int(input())
Cowlist = [-1 for v in range(11)]
count = 0

for i in range(casecount):
  Cownum, location = map(int, input().split())
  if Cowlist[Cownum] != location:
    if Cowlist[Cownum] != -1:
      count += 1
    Cowlist[Cownum] = location
      
print(count)
