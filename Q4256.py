TestCase = int(input())
for x in range(TestCase):
    #Take input
    Length = int(input())
    PreOrder = list(map(int, input().split()))
    InOrder = list(map(int, input().split()))
    PostOrder = []

    def Divide(preorder, inorder):
        if len(preorder) == 0:
            return

        elif len(preorder) == 1:
            print(preorder[0], end = " ")
            return
        #If there is only 2 nodes in preorder, first one must be the root while the second one is the node
        #It doesn't apply when there are three because left and right needs to be recognised
        elif len(preorder) == 2:
            print(preorder[1], preorder[0], end = " ")
            return


        root_pos = inorder.index(preorder[0])
        
        #Divide it left and right with inorder and postorder and repeat
        #Print the left first
        left_inorder = inorder[0:root_pos]
        left_preorder = preorder[1:len(left_inorder)+1]
        Divide(left_preorder, left_inorder)
        
        #Print the right second
        right_inorder = inorder[root_pos+1:]
        right_preorder = preorder[len(left_preorder)+1:]
        Divide(right_preorder, right_inorder)
        
        #Print the root last
        print(preorder[0], end = " ")
    
    #Execute function
    Divide(PreOrder, InOrder)
    print()
