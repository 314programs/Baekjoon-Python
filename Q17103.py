import sys
input = sys.stdin.readline
CaseCount = int(input())
CaseList = []

#Use sieve of eratosthenes to get list of prime numbers
def PrimeList(n):
    sieve = [True]*(n+1)
    m = int((n+1)**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
                
    return sieve

#Take input and change item 0 and 1 of Primelist since 1 and 0 is not a prime
for v in range(CaseCount):
    CaseList.append(int(input()))
    
Primes = PrimeList(max(CaseList))
Primes[0] = False
Primes[1] = False

#Use testcase list to see possible combinations
for item in CaseList:
    Count = 0
    for i in range(item//2 + 1):
        if Primes[item - i] == True and Primes[i] == True:
            Count += 1
            
    print(int(Count))
