TestCase = int(input())
for a in range(TestCase):
  Answer = int(input())
  Dp = [1,1,1]

  for i in range(3,Answer):
    Dp.append(Dp[i-3]+Dp[i-2])

  print(Dp[-1])
