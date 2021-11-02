num = int(input())
if num == 1:
    print('*')
    
else:
    StarList = ['*',' ']*((num//2) + 1)
    for i in range(1,(num*2) + 1):
        if i%2 != 0:
            print(''.join(StarList[0:num]).rstrip())
        else:
            print(''.join(StarList[1:num+1]).rstrip())
