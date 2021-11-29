num = int(input())
s = (num*2)-1
for i in range(s, 0, -2):
    print(' '*((s-i)//2) + '*'*i)
