#Very lazy and inefficient writing
Total = []
SetList = []
MaxCount = 0
Mode = 0

for i in range(10):
    num = int(input())
    Total.append(num)
    if num not in SetList:
        SetList.append(num)
        
for item in SetList:
    if MaxCount < Total.count(item):
        MaxCount = Total.count(item)
        Mode = item
    
print(sum(Total)//10)
print(Mode)

