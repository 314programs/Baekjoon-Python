testCase = int(input())
Cute = 0
NotCute = 0
for i in range(testCase):
    num = int(input())
    if num == 0: NotCute += 1
    else: Cute += 1
if NotCute > Cute:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
