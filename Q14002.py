#O(N^2) LIS algorithm
list_len = int(input())
num_list = list(map(int, input().split()))
DP = [1 for v in range(list_len)]

for i in range(list_len):
    for j in range(i):
        if num_list[i] > num_list[j]:
            DP[i] = max(DP[i], DP[j]+1)

#Print longest LIS length
max_DP = max(DP)
print(max_DP)

#Finding out LIS using index of the longest LIS length
result = []
max_index = DP.index(max_DP)

#Because DP list saves up all the length, we can use the index of maximum index to find out the sequence
#Subtract 1 from maximum index until 0. Since its going from longest length... to 0, it needs to be reversed when printed
while max_index >= 0:
    if DP[max_index] == max_DP:
        result.append(num_list[max_index])
        max_DP -= 1
    max_index -= 1
result.reverse()
#Just learned about this simple trick
print(*result)

