Number = int(input())
LineNumMid = (Number-1)*2

for i in range(1, LineNumMid+2, 2):
  print(' '*((Number*2 - i)//2) + '*'*i)
for i in range(LineNumMid-1, 0, -2):
  print(' '*((Number*2 - i)//2) + '*'*i)
