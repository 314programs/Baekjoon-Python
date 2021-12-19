n = int(input())
Fib = [0]*(n+1)
Fib[0] = 1
Fib[1] = 1
for i in range(2, n):
    Fib[i] = Fib[i-1] + Fib[i-2]
print(Fib[n-1])
