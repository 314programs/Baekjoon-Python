#Solved long time ago but couldn't understand
#Made new code that I can understand
import heapq
import sys
input = sys.stdin.readline

TestCase = int(input())
for x in range(TestCase):
    Length = int(input())
    #Make dictionary and size so that I don't have to constantly update both heaps
    Dictionary = {}
    Size = 0
    
    #Two heaps for minimum and maximum
    Min_Heap = []
    Max_Heap = []

    for x in range(Length):
        commend, num = map(str, input().split())
        num = int(num)
        
        #Insert function: Inserts number into both heaps and updates dictionary and size
        if commend == 'I':
            heapq.heappush(Min_Heap, num)
            heapq.heappush(Max_Heap, -num)
            
            if num not in Dictionary:
                Dictionary[num] = 1
            else:
                Dictionary[num] += 1
            
            Size += 1
             
        else:
          #Delete from heap accordingly if heap is not empty
          #Update dictionary too
            if Size != 0:
                if num == 1:
                    while Max_Heap:
                        Popped = -heapq.heappop(Max_Heap)
                        if Dictionary[Popped] != 0:
                            Dictionary[Popped] -= 1
                            break
                    
                else:
                    while Min_Heap:
                        Popped = heapq.heappop(Min_Heap)
                        if Dictionary[Popped] != 0:
                            Dictionary[Popped] -= 1
                            break
                
                Size -= 1
    
    #Update both heaps by using the dictionary
    while Max_Heap and Dictionary[-Max_Heap[0]] == 0: heapq.heappop(Max_Heap)
    while Min_Heap and Dictionary[Min_Heap[0]] == 0: heapq.heappop(Min_Heap)
    
    #Print
    if Size != 0:
        print(-Max_Heap[0], Min_Heap[0])
    else:
        print('EMPTY')
            
