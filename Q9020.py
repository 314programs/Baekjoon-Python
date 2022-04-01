#Planting grass
testcase = int(input())
Prime_temp = [0 for v in range(10001)]
Prime_temp[0] = 1
Prime_temp[1] = 1

for i in range(2, int(10000**0.5)+1):
    if Prime_temp[i] == 0:
        for x in range(i+i, 10001, i):
            Prime_temp[x] = 1

Prime = [v for v in range(10001) if Prime_temp[v] == 0]

for case in range(testcase):
    num = int(input())
    min_diff = float('inf')
    ans = [0,0]

    for item in Prime:
        if item > num:
            break
        if Prime_temp[num - item] == 0 and min_diff > abs(item-(num-item)):
            min_diff = abs(item-(num-item))
            ans = [item, num-item]

    ans.sort()
    print(ans[0], ans[1])

