People = 0
Result = 0
for i in range(10):
    Out, In = map(int, input().split())
    People -= Out
    People += In
    Result = max(Result, People)
print(Result)
