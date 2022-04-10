import sys
input = sys.stdin.readline

testcase = int(input())
for i in range(testcase):
    numlist = list(map(int, input().split()))
    total = 0
    minimum = 101
    for item in numlist:
        if item%2 == 0:
            total += item
            minimum = min(item, minimum)
    
    print(total, minimum)
