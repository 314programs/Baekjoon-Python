Max_amount = 2715**2
Visited = [0 for v in range(Max_amount)]
Visited[0] = -1
Visited[1] = -1

for i in range(2, int(Max_amount**0.5) + 1):
    if Visited[i] == 0:
        for j in range(i+i, Max_amount, i):
            Visited[j] = -1

Prime = [v for v in range(Max_amount) if Visited[v] == 0]

num = int(input())
print(Prime[num-1])
