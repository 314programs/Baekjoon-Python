#LIS O(nlogn) alogrithm using bisect
import bisect

list_len = int(input())
num_list = list(map(int, input().split()))

DP = [num_list[0]]

for i in range(list_len):
  #If current number is bigger then last item of DP, it is an increasing sequence so append it in
    if num_list[i] > DP[-1]:
        DP.append(num_list[i])
    else:
        #bisect.bisect_left returns position of biggest items index
        index = bisect.bisect_left(DP, num_list[i])
        #Update DP
        DP[index] = num_list[i]
print(len(DP))
