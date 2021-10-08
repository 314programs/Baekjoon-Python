#There is a simpler method but I wanted to study the algorithm using modular exponentiation
a1,b1,c1 = map(int, input().split())

def power(a,b):
#If the power is 1 or 0, return value
    if b == 1:
        return a%c1
    elif b == 0:
        return 0
#To avoid O(n), divide the power by 2 and multiply and base by itself(following log rules)
    else:
        temp = power(a,b//2)
#If its even just divide the temp^2 by c
        if b%2 == 0:
            return (temp*temp)%c1
#If its odd  divide the temp^2 times a by c, since a was rounded off
        else:
            return (temp*temp*a)%c1
            
print(power(a1,b1))




