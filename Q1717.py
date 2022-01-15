#I need to practice on union find, so I decided to solve this question first
#sys for speedy input and recursion limit
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

NodeNum, CaseNum = map(int, input().split())
parent = [v for v in range(NodeNum+1)]

#Find the parent therefore in union
def FindParent(target):
    if target == parent[target]:
        return target
    parent[target] = FindParent(parent[target])
    return parent[target]

#Make a and b union
def Union(a,b):
    a = FindParent(a)
    b = FindParent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#Check input and print accordingly
for i in range(CaseNum):
    a,b,c = map(int, input().split())
    if a == 0:
        Union(b, c)
        
    else:
        if FindParent(b) == FindParent(c):
            print('YES')
        else:
            print('NO')
            
