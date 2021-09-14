#Input and setup
TestCase = int(input())
for a in range(TestCase):
  Answer = int(input())
  Dp = [1,1,1]
#Using memoization to store answers
  for i in range(3,Answer):
    Dp.append(Dp[i-3]+Dp[i-2])
#Print the last(index of Answer-1) element
  print(Dp[-1])
