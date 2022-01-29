#I used the pisano period to reduce the time taken
#I found the pisano period by running a while loop which was 1500000
Num = int(input())
Num %= 1500000
Pibonacci = [1,1]
for i in range(2, Num):
    Pibonacci.append(Pibonacci[i-2] + Pibonacci[i-1]%1000000)
print(Pibonacci[-1]%1000000)
