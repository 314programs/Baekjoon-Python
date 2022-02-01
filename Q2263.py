import sys
sys.setrecursionlimit(10**5)
Length = int(input())
InOrder = list(map(int, input().split()))
PostOrder = list(map(int, input().split()))
Dictionary = [0 for i in range(Length+1)]

#Make a dictionary so that I don't have to use index() each time
for i in range(Length):
    Dictionary[InOrder[i]] = i


def Divide(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end:
        return
    
    root_pos = Dictionary[PostOrder[postorder_end]]
    print(PostOrder[postorder_end], end = " ")
    
    if postorder_end == postorder_start:
        return
    
    Dif = root_pos - inorder_start
    #If I made a list of left and right inorder and postorder it would cost too much memory
    #Instead of slicing to make new lists, starting and ending indexs are used
    Divide(inorder_start, root_pos-1, postorder_start, postorder_start + Dif - 1)
    Divide(root_pos+1, inorder_end, postorder_start + Dif, postorder_end-1)
    
Divide(0, Length-1, 0, Length-1)
