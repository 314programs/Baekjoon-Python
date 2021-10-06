import sys
Num = int(sys.stdin.readline())
Count = 0
for i in range(1, Num+1):
    n = str(i)
    Count += n.count('3') + n.count('6') + n.count('9')
        
sys.stdout.write(str(Count))
