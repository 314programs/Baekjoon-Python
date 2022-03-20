list_len = int(input())
num_list = list(map(int, input().split()))

#Maximum sum ending with the number
DP_end = [0 for v in range(list_len)]
DP_end[0] = num_list[0]

for i in range(1,list_len):
    DP_end[i] = max(DP_end[i-1] + num_list[i], num_list[i])

#Maximum sum starting with the number
DP_start = [0 for v in range(list_len)]
DP_start[list_len-1] = num_list[list_len-1]

for i in range(list_len-2, 0, -1):
    DP_start[i] = max(DP_start[i+1] + num_list[i], num_list[i])

#Maximum sum without removing a number
maximum = max(DP_start)

#Maximum sum with removing a number
for i in range(1, list_len-1, 1):
    maximum = max(maximum, DP_end[i-1] + DP_start[i+1])

print(maximum)
