#Split input
num1, num2 = input().replace(':', ' ').split()
a, b = int(num1), int(num2)
R = a%b
#Use euclidean algorithm to find the HCF
while R:
  a = b
  b = R
  R = a%b

print(str(int(num1)//b) + ':' + str(int(num2)//b))
