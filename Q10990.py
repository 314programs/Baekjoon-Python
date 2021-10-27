num = int(input())
print(' '*(num-1)+'*')
for i in range(2,num+1):
    print(' '*(num-i)+'*'+' '*(((i-2)*2) + 1) + '*')
