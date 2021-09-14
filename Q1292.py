Start, End = map(int, input().split())
NumList = []
for a in range(1,End+1):
  for b in range(a):
    NumList.append(a)

  if len(NumList) == End:
    break

print(sum(NumList[Start-1:End]))
