#Listening to baekjoon but memset doesn't exist here so had to improvise
import sys
input = sys.stdin.readline

testcase = int(input())
for case in range(testcase):
    list_len = int(input())
    cost_list = list(map(int, input().split()))
    DP = [[-1]*(list_len) for v in range(list_len)]

    def find_min(start, end):
        #No cost
        if start == end:
            return 0
        #Cost already calculated
        if DP[start][end] != -1:
            return DP[start][end]
        #Just combine 2 of them for cost
        if end - start == 1:
            DP[start][end] = cost_list[start] + cost_list[end]
            return DP[start][end]

        sum_ = sum(cost_list[start:end+1])
        ans = DP[start][end]
  
        for i in range(start, end):
            #Divide problem into smaller ones
            temp = find_min(start, i) + find_min(i+1, end) + sum_
            #If smaller or unrecorded
            if ans == -1 or ans > temp:
                ans = temp
        DP[start][end] = ans
        return ans
    
    print(find_min(0, list_len-1))
    
