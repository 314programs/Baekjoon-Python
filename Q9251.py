Word1 = input()
Word2 = input()

#Make DP List
DP = [[0 for v in range(len(Word2)+1)] for i in range(len(Word1)+1)]

    
for o in range(len(Word1)+1):
    for t in range(len(Word2)+1):
        if o == 0 or t == 0:
            DP[o][t] = 0
        #If they are equal, it would be the previous result +1
        elif Word1[o-1] == Word2[t-1]:
            DP[o][t] = DP[o-1][t-1] + 1
        #Else choose the maximum from previous
        else:
            DP[o][t] = max(DP[o][t-1], DP[o-1][t])

    
print(DP[len(Word1)][len(Word2)])
