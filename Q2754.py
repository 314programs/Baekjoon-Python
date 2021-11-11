Word = input()
Result = 0
if Word[0] == 'A':
    Result += 4.0
elif Word[0] == 'B':
    Result += 3.0
elif Word[0] == 'C':
    Result += 2.0
elif Word[0] == 'D':
    Result += 1.0
else:
    Result = 0.0
    
if Word[1] == '+':
    Result += 0.3
elif Word[1] == '-':
    Result -= 0.3
print(Result)
