#Practicing using O(nlogn) LIS algorithm and dynamic programming
import bisect
Soldier_num = int(input())
Soldiers = list(map(int, input().split()))

Soldiers.reverse()

Count = 0
DP = [Soldiers[0]]

for i in range(1, Soldier_num):
    if Soldiers[i] > DP[-1]:
        DP.append(Soldiers[i])
    else:
        #Still need to update for future count
        index = bisect.bisect_left(DP, Soldiers[i])
        DP[index] = Soldiers[i]
        #Just add count
        Count += 1

print(Count)
