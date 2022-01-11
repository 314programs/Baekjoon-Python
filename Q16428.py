#Why is this in bronze 4?????
#Should be at least bronze 2 in my opinion

a,b = map(int, input().split())
if a == 0:
    print('0')
    print('0')
else:
    if a > 0 and b > 0:
        print(a//b)
        print(a%b)
    elif a > 0 and b < 0:
        if a%b != 0:
            print(a//b + 1)
            print(abs(b) + a%b)
        else:
            print(a//b)
            print(0)
    elif a < 0 and b > 0:
        print(a//b)
        print(a%b)
    else:
        if a%b != 0:
            print(a//b+1)
            print(a%b + abs(b))
        else:
            print(a//b)
            print(0)
