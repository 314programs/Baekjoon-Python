import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

Gate_Num = int(input())
Plane_Num = int(input())

Gate = [v for v in range(Gate_Num+1)]
Docked = 0

#Finding parents
def find_parent(target):
    if Gate[target] == target:
        return target
    Gate[target] = find_parent(Gate[target])
    return Gate[target]

for i in range(Plane_Num):
    Current_Plane = int(input())
    Temp = find_parent(Current_Plane)
    if Temp == 0:
        break
    #Instead of union() just -1 the value to save time
    Gate[Temp] = Temp - 1
    Docked += 1

print(Docked)
