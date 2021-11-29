num = int(input())
for i in range(1,num+1):
    layer = ((num-i)*' ' + '* '*i)
    print(layer.rstrip())
