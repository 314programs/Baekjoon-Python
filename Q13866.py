Teamlist = list(map(int, input().split()))
Teamlist.sort()
print(abs((Teamlist[0]+Teamlist[3])-(Teamlist[2]+Teamlist[1])))
