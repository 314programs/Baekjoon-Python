#I need to practice knapsack alogorithm
Time, Chapter = map(int, input().split())
Day = []
Page = []
for i in range(Chapter):
    d, p = map(int, input().split())
    Day.append(d)
    Page.append(p)


DP = [[0 for x in range(Time+1)] for v in range(Chapter+1)]

for p in range(1, Chapter+1):
    for d in range(1, Time+1):
        Current_Page = Page[p-1]
        Current_Day = Day[p-1]
        
        if d < Current_Day:
            DP[p][d] = DP[p-1][d]
        else:
          #I always forget how to do this part
            DP[p][d] = max(DP[p-1][d], Current_Page + DP[p-1][d-Current_Day])
            
print(DP[-1][-1])
