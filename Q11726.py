#Take input and set up a list
Width = int(input())
DP = [int(i) for i in range(Width+1)]

#Use memoization to stored added values
for i in range(3, Width+1):
  DP[i] = DP[i-1] + DP[i-2]
print(DP[Width]%10007)
