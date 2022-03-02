#I should revise two pointer as I couldn't solve this problem well
#Basic set up
Chemical_num = int(input())
Chemicals = list(map(int, input().split()))
Answer = float('inf')
Answer_Chemicals = [-1, -1, -1]
Chemicals.sort()

#O(N^2) as mid will be decided through a loop
for mid in range(1, Chemical_num-1):
    start = 0
    end = Chemical_num-1
    
    #Use two pointer
    while start < mid < end:
        total = Chemicals[start] + Chemicals[mid] + Chemicals[end]

        if abs(total) < Answer: 
            Answer = abs(total)
            Answer_Chemicals = [Chemicals[start], Chemicals[mid], Chemicals[end]]
        
        if total < 0:
            start += 1
        else:
            end -= 1

print(' '.join(map(str, Answer_Chemicals)))
        
