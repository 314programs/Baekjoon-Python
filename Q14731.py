#I had simpler code using pow but decided I need to revise on making power functions
import sys
input = sys.stdin.readline
N = int(input())

def pow_function(number, power, divider):
    if power == 1:
        return number%divider
    if power == 0:
        return 1

    temp = pow_function(number, power//2, divider)
    if power%2 == 0:
        return (temp*temp)%divider
    else:
        return (temp*temp*number)%divider


total = 0
for case in range(N):
    num, pow_ = map(int, input().split())
    if pow_ == 0: multiply = 0
    else: multiply = pow_function(2, pow_-1, 10**9 + 7) % (10**9 + 7)
    total += (num*pow_) * multiply

print(total % (10**9 + 7))
