num = int(input())
if num > 1:
    print(' '*(num-1) + '*')
    Count = 1
    for i in range(1,num-1):
        print(' '*(num-1-i) + '*' + ' '*(Count) + '*')
        Count += 2
    print('*'*((num*2)-1))
else:
    print('*')
