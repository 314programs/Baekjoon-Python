#Requires fast input and output
import sys
input = sys.stdin.readline

list_length = int(input())
num_list = list(map(int, input().split()))
testcase = int(input())

DP = [[0] * list_length for v in range(list_length)]

#Length of 1 must be palindrome
for i in range(list_length):
    DP[i][i] = 1

#Lenght of 2 must be palindrome is they are the same
for i in range(list_length-1):
    if num_list[i] == num_list[i+1]:
        DP[i][i+1] = 1

#For each length
for k in range(2, list_length):
    #Start from where
    for i in range(0, list_length-k):
        #Check if outer layer and inner layer is is both palindrome
        if num_list[i] == num_list[i+k] and DP[i + 1][i + k - 1] == 1:
            DP[i][i+k] = 1

for i in range(testcase):
    s, e = map(int, input().split())
    sys.stdout.write(str(DP[s-1][e-1]) + '\n')
