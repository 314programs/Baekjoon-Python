#Overflow in c++, so using python instead
import sys
input = sys.stdin.readline

for i in range(3):
    num_cnt = int(input())
    total = 0
    for j in range(num_cnt):
        total += int(input())
    
    if(total == 0):
        print(0)
    elif(total > 0):
        print("+")
    else:
        print("-")
