# # #   BFS   # # #
# Idea: Queue(FIFO)
# Pseudo-code

def BFS(self, root):
    if root == None:
        return
    Que = []     # Que to store the node
    Val = []     # Val to store the value
    Que.append(root)
    while Que:
        # Take the first element in Que
        currNode = Que.pop(0)
        Val.append(currNode.val)
        # print(currNode.val, end=' ')
        if currNode.left:
            Que.append(currNode.left)
        if currNode.right:
            Que.apend(currNode.right)
    return Val
