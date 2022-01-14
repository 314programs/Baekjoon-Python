import sys
input = sys.stdin.readline

DiceNum = int(input())
ans = 0
divide = 10**9 + 7

#Making my own pow() function
def power(num, thepow):
    if thepow == 1:
        return num%divide
    else:
        temp = power(num, thepow//2)
        if thepow%2 == 0:
            return (temp*temp)%divide
        else:
            return (temp*temp*num)%divide
            

for i in range(DiceNum):
    #Store fraction as a list
    Fraction = list(map(int, input().split()))
    
    #power(Fraction[0], 10**9 + 5) is the b^-1 
    #Add all answers together
    ans += (Fraction[1]*power(Fraction[0], 10**9 + 5))%divide
    ans %= divide
    
print(ans)



