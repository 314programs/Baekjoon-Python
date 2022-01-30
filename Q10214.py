testcase = int(input())
for x in range(testcase):
    y, k = 0,0
    for i in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y > k:
        print('Yonsei')
    elif k > y:
        print('Korea')
    else:
        print('Draw')
