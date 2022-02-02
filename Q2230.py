Length, Minimum = map(int, input().split())
NumList = [int(input()) for v in range(Length)]
NumList.sort()
MinVal = float('inf')

Start = 0
End = 0

#Two pointer
while True:
    if NumList[End] - NumList[Start] < Minimum:
        End += 1   
    elif NumList[End] - NumList[Start] >= Minimum:
        MinVal = min(MinVal, NumList[End] - NumList[Start])
        Start += 1

    if End == Length or Start == Length:
        break
    
print(MinVal)
