#I need to practice stacks because I am not experienced with them
from collections import deque

Placement = input()
Pieces = 0
count = 0
stack = deque([])
for i in range(len(Placement)):
    char = Placement[i]
    if char == '(':
        stack.append(')')
    elif char == ')':
        if i > 0 and Placement[i-1] == '(':
            Pieces += len(stack)-1
        else:
            Pieces += 1
        stack.popleft()
        
print(Pieces)
        
        
