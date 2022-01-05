#Even more USACO bronze
testcase = int(input())
CowList = []
CurrentTime = 0
for i in range(testcase):
    CowList.append(list(map(int, input().split())))

#Simple greedy algorithm by sorting
CowList.sort(key = lambda x: (x[0], x[1]))
for start_time, time_taken in CowList:
    if CurrentTime < start_time:
        CurrentTime = start_time
    CurrentTime += time_taken

print(CurrentTime)
