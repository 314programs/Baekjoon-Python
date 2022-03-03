#Learning to use LCS algorithm again...
Word1 = input()
Word2 = input()

DP = [['' for v in range(len(Word2)+1)] for v in range(len(Word1)+1)]

#Instead of using max length as variable, use the word instead
#Use the length of the word for the DP instead
for i in range(1, len(Word1)+1):
    for x in range(1, len(Word2)+1):
        if Word1[i-1] == Word2[x-1]:
            DP[i][x] += DP[i-1][x-1] + Word1[i-1]
        else:
            if len(DP[i-1][x]) > len(DP[i][x-1]):
                DP[i][x] = DP[i-1][x]
            else:
                DP[i][x] = DP[i][x-1]

print(len(DP[-1][-1]))
if len(DP[-1][-1]) != 0:
    print(DP[-1][-1])

    
