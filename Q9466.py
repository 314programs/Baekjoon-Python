import sys
from collections import deque
input = sys.stdin.readline

def Find_cycle(start):
    global No_group
    Grouping = [start]
    Current_node = start
    Visited[start] = start + 1

    while True:
        Current_node = Preference[Current_node]-1
        #Add new student to grouping
        if Visited[Current_node] == 0:
          #Use start + 1 to distinguish groups in visited
            Visited[Current_node] = start+1
            Grouping.append(Current_node)
        else:
          #If there is a cycle
            if Current_node == Grouping[0]:
                return
          #If there is a cycle inside the group but not a complete cycle
            elif Visited[Current_node] == start+1:
              #edit visited marks of the cycle and the part that is not in cycle
                Temp = Grouping.index(Current_node)
                for i in range(Temp):
                    Visited[Grouping[i]] = -1
                    No_group += 1
                for i in range(Temp, len(Grouping)):
                    Visited[Grouping[i]] = Current_node + 1
                
                Visited[start] = -1
                return
          #If there is no cycle
            else:
                No_group += 1
                #Remove visited marks
                for item in Grouping:
                    Visited[item] = 0
                Visited[start] = start+1
                return


case_count = int(input())
#Input
for case in range(case_count):
    Student_num = int(input())
    Preference = list(map(int, input().split()))
    No_group = 0

    Visited = [0 for v in range(Student_num)]

    for i in range(Student_num):
        if Visited[i] == 0:
            Find_cycle(i)

    print(No_group)
