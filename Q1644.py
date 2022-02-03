num = int(input())

sieve = [1 for v in range(num+1)]
sieve[0] = 0
sieve[1] = 0

#Sieve of Eratosthenes
for i in range(2, int(num**0.5)+1):
    if sieve[i] == 1:
        for x in range(i+i, num+1, i):
            sieve[x] = 0
            
primes = [v for v in range(2, num+1) if sieve[v] == 1]

start = 0
end = 0
count = 0

#Two pointer
while True:
    if start >= len(primes) or end >= len(primes):
        break
    
    #Since it has to be sum of a sequence, a loop can be used
    temp = 0
    for i in range(start, end+1):
        temp += primes[i]
        if temp == num:
            start += 1
            count += 1
            break
        
        if temp > num:
            start += 1
            break

    if temp < num:
        end += 1
        
print(count)
