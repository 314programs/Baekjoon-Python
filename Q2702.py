caseCount = int(input())
for i in range(caseCount):
  a, b = map(int, input().split())
  num1, num2 = a,b

  R = a%b
  while R:
    a = b
    b = R
    R = a%b
  
  print((num1*num2)//b, b)
