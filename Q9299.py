#Wanted to try out calculus
testcase = int(input())
for case in range(testcase):
    temp = list(map(int, input().split()))
    power = temp[0]
    polynomial = temp[1:]
    result = []

    for i in range(power, 0, -1):
        result.append(i*polynomial[power-i])

    print('Case ' + str(case + 1) + ': ', end = "")
    print(power-1, end = " ")
    print(' '.join(map(str, result)))
