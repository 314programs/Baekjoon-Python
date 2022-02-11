import sys
input = sys.stdin.readline

Height, Width = map(int, input().split())
Alphabet_List = [list(map(str, input())) for v in range(Height)]
#Visited dictionary for alphabets
Visited_Dict = [0 for v in range(26)]

Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

max_distance = 0

def Backtrack(depth, coord_x, coord_y):
    global max_distance
    for i in range(4):
        new_x = coord_x + Dx[i]
        new_y = coord_y + Dy[i]
        
        #Check if new coordinate is within limits of the graph and is an alphabet that was not visited before
        if -1 < new_x < Width and -1 < new_y < Height and Visited_Dict[ord(Alphabet_List[new_y][new_x]) - 65] == 0:
            #Mark the visit, back track and unmark
            Visited_Dict[ord(Alphabet_List[new_y][new_x]) - 65] = 1
            Backtrack(depth + 1, new_x, new_y)
            Visited_Dict[ord(Alphabet_List[new_y][new_x]) - 65] = 0

    max_distance = max(max_distance, depth)
    return

#Start from top left, mark the beginning first
Visited_Dict[ord(Alphabet_List[0][0]) - 65] = 1
Backtrack(1, 0, 0)
print(max_distance)
