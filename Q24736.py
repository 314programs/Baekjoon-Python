#Doing something important, so bronze 5 for the day
a = list(map(int, input().split()))
b = list(map(int, input().split()))

scoring = [6,3,2,1,2]

for i in range(5):
    a[i] *= scoring[i]
    b[i] *= scoring[i]
    
print(sum(a), sum(b))
