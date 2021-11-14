Max = 0
Current = 0
for i in range(4):
    Subtract, Add = map(int, input().split())
    Current += Add
    Current -= Subtract
    
    if Current > Max:
        Max = Current
print(Max)
    
    
