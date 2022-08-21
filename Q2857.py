import sys
input = sys.stdin.readline

printed = False
for i in range(5):
    name = input()
    if "FBI" in name:
        printed = True
        print(i+1)

if printed == False:
    print("HE GOT AWAY!")
