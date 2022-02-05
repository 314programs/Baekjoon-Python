#Checking in with a bronze as my exams are coming
Chang = 100
Sang = 100

testCase = int(input())
for i in range(testCase):
    C, S = map(int, input().split())
    if C > S:
        Sang -= C
    elif C < S:
        Chang -= S
    
print(Chang)
print(Sang)
