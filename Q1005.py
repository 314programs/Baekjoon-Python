import sys
from collections import deque
input = sys.stdin.readline

Testcase = int(input())
for casecount in range(Testcase):
    #Take in input(large)
    Building_num, Building_Connections_num = map(int, input().split())
    Building_time = list(map(int, input().split()))
    Building_Connections = [list(map(int, input().split())) for v in range(Building_Connections_num)]
    Winning_Building = int(input())
    
    #Set up graphs for memoization and storing connections (indegrees)
    Indegrees = [[] for v in range(Building_num+1)]
    Time_Taken = [-1 for v in range(Building_num + 1)]

    for need, build in Building_Connections:
        Indegrees[build].append(need)
  
    
    #DP using recursion and memoization
    #Working from target building to backwards
    def Find_Min(building):
        if Time_Taken[building] == -1:
            max_val = -1
            for item in Indegrees[building]:
                max_val = max(Find_Min(item), max_val)

            if max_val == -1:
                max_val = 0

            Time_Taken[building] = max_val + Building_time[building-1]

        return Time_Taken[building]
            
    print(str(Find_Min(Winning_Building)))
