import sys
#sys for speed
num = int(sys.stdin.readline())

#For checking if there was a factor other than 1 or itself
Appended = False
if num != 1:
    while True:
        Appended = False
#Loop until square root of of the number to avoid repetition
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                num //= i
                sys.stdout.write(str(i)+'\n')
                Appended = True
                break
#If there was no factor, print the number and end
        if not Appended:
            sys.stdout.write(str(num)+'\n')
            break
