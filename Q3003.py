Temp = list(map(int, input().split()))
Format = [1,1,2,2,2,8]

for i in range(6):
    Format[i] -= Temp[i]
print(' '.join(map(str, Format)))
