E,S,M = map(int, input().split())
Year = 0

while True:
    Year += 1
    if (Year-E)%15 == 0 and (Year-S)%28 == 0 and (Year-M)%19 == 0:
        print(Year)
        break

