ListLen = int(input())
#Sort one ascending and other decending so that highest value pairs up with lowest value
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse = True)
B.sort()

#Multiply and add up
Result = 0 
for i in range(ListLen):
    Result += A[i] * B[i]
print(Result)
