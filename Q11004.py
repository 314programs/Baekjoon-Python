#There was no need to quicksort, this can do
import sys
ListLen, k = map(int, sys.stdin.readline().split())
NumList = list(map(int, sys.stdin.readline().split()))
NumList.sort()
print(NumList[k-1])
