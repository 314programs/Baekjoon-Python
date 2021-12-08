#Range is too large to use BFS
start, end = map(int, input().split())
Count = 1
Stop = False

#Start from the end
while start != end:
    Count += 1

    if end%10 == 1 and len(str(end)) > 1:
        end = int(str(end)[:len(str(end))-1])
    elif end//2 == end/2:
        end //= 2
    else:
        Stop = True
        break
        
if not Stop: print(Count)
else: print('-1')
