num = int(input())
Spaces = 2*(num-2) + 1
Result = []
Result.append('*'*num + ' '*Spaces + '*'*num)
for i in range(1, num -1):
    Result.append(' '*i + '*' + ' '*(num-2) + '*' + ' '*(Spaces-(2*i)) + '*' + ' '*(num-2) + '*')
    
Result.append((num-1)*' ' + '*' + ' '*(num-2) + '*' + ' '*(num-2) + '*')

for i in range(num-2, 0, -1):
    Result.append(' '*i + '*' + ' '*(num-2) + '*' + ' '*(Spaces-(2*i)) + '*' + ' '*(num-2) + '*')
    
Result.append('*'*num + ' '*Spaces + '*'*num)

for item in Result:
    print(item)
