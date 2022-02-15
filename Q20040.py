#I like union finders now
#This question needs union finding algorithm since it wants a cycle of points
import sys
input = sys.stdin.readline

#Take input
Nodes, Connections = map(int, input().split())
Connection_List = [list(map(int, input().split())) for v in range(Connections)]
Parent = [v for v in range(Nodes)]
Game_Finish = False

def Find_Parent(target):
    if Parent[target] == target:
        return target
    Parent[target] = Find_Parent(Parent[target])
    return Parent[target]

def Union(a,b):
    a = Find_Parent(a)
    b = Find_Parent(b)

    if a < b:
        Parent[b] = a
    else:
        Parent[a] = b

#Detecting when there is a cycle
for i in range(Connections):
    start, end = Connection_List[i]
    if Find_Parent(start) != Find_Parent(end):
        Union(start, end)
    else:
        Game_Finish = True
        print(i + 1)
        break

if Game_Finish == False:
    print(0)


