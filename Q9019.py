from collections import deque
import sys
input = sys.stdin.readline

TestCase = int(input())
for i in range(TestCase):
    CurrentNum, NeededNum = map(int, input().split())
    queue = deque([[CurrentNum, '']])
    Visited = [0]*10001
    Visited[CurrentNum] = 1
#Use BFS
    while queue:
        temp = queue.popleft()

        if temp[0] == NeededNum:
            print(temp[1])
            break
        #D
        if Visited[(temp[0]*2) % 10000] == 0:
            Visited[(temp[0]*2) % 10000] = 1
            queue.append([(temp[0]*2) % 10000, temp[1]+'D'])

        SubtractNum = temp[0]
        if SubtractNum == 0:
            SubtractNum = 9999
        else:
            SubtractNum -= 1

        #S
        if Visited[SubtractNum] == 0:
            Visited[SubtractNum] = 1
            queue.append([SubtractNum, temp[1]+'S'])

        #L
        if len(str(temp[0])) == 4:
            LeftSpin = int(str(temp[0])[1:len(str(temp[0]))]+ str(temp[0])[0])
        else:
            LeftSpin = int(str(temp[0]) + '0')

        if Visited[LeftSpin] == 0:
            Visited[LeftSpin] = 1
            queue.append([LeftSpin, temp[1] + 'L'])


        #R
        if len(str(temp[0])) == 4:
            RightSpin = int(str(temp[0])[-1] + str(temp[0])[0:len(str(temp[0]))-1])
        else:
            RightSpin = int(str(temp[0])[-1] + '0'*(4-len(str(temp[0]))) + str(temp[0])[0:len(str(temp[0]))-1])
        
        if Visited[RightSpin] == 0:
            Visited[RightSpin] = 1
            queue.append([RightSpin, temp[1] + 'R'])
