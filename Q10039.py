Total = 0
for i in range(5):
    Score = int(input())
    if Score < 40:
        Score = 40
    Total += Score
print(Total//5)
