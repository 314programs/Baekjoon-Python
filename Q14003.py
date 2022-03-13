#LIST O(nlogn) algorithm
import bisect
list_len = int(input())
num_list = list(map(int, input().split()))
DP = [num_list[0]]

#Use a counter to measure sequence with longest length that can be produced in the index
Counter = [1 for v in range(list_len)]

#Update the counter using its index
for x in range(list_len):
    if num_list[x] > DP[-1]:
        DP.append(num_list[x])
        Counter[x] = len(DP)
    else:
        index = bisect.bisect_left(DP, num_list[x])
        DP[index] = num_list[x]
        Counter[x] = index+1

#Print length first
max_length = len(DP)
print(max_length)

max_index = Counter.index(max_length)
result = []

#Use the same technique used in 14002 to print the sequence
while max_index >= 0:
    if Counter[max_index] == max_length:
        result.append(num_list[max_index])
        max_length -= 1
    max_index -= 1

result.reverse()
print(*result)
