#Maths test tomorrow sad
max_score = 0
num = 0
for i in range(5):
    scores = list(map(int, input().split()))
    if max_score < sum(scores):
        max_score = sum(scores)
        num = i + 1
print(num, max_score)
