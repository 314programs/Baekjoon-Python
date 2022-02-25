#USACO today, gonna fail
num = int(input())
Total = 0
for i in range(num):
    student, apple = map(int, input().split())
    Total += apple%student
print(Total)
