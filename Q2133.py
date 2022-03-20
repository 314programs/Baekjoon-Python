Width = int(input())
#Odd numbers are impossible to make
if Width%2 != 0:
    print(0)
else:
    Width //= 2
    DP = [0 for v in range(16)]
    #Initial value
    DP[0] = 1

    for i in range(1, Width+1):
        #Previous value *3 since there can be 3 types of arrangements in 2*3 space
        DP[i] = DP[i-1] * 3
        for x in range(2, i+1):
            #New blocks can be formed
            DP[i] += DP[i-x]*2
    print(DP[Width])
