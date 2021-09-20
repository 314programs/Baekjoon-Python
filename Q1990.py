import sys
StartPoint, EndPoint = map(int, sys.stdin.readline().split())
#Check if number is a palindrome number
def Palindrome(Num):
  if str(Num) == str(Num)[::-1]:
    return True
  return False
#Check if number is a prime number
def Prime(Num):
  for i in range(2, int(Num**0.5)+1):
    if Num%i == 0:
      return False
  return True
#For starting number to ending number, loop and check with functions above.
for i in range(StartPoint, EndPoint+1):
  if Palindrome(i):
    if Prime(i):
      sys.stdout.write(str(i) + '\n')
  if i >= 9989899:
    break

sys.stdout.write('-1' + '\n')
