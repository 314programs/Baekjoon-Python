import math
nums = list(map(int, input()))
num_count = [0 for v in range(9)]
for item in nums:
    if item != 9:
        num_count[item] += 1
    else:
        num_count[6] += 1

maximum = 0

for i in range(9):
    item = num_count[i]
    if i == 6:
        maximum = max(math.ceil(item/2), maximum)
    else:
        maximum = max(item, maximum)
print(maximum)
