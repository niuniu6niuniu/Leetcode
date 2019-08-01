# # #   DFS   # # #
# Idea: Stack(FILO)
# Pseudo-code

def DFS(self, root):
    if root == None:
        return
    Stack = []
    Val = []
    Stack.append(root)
    Val.append(root.val)
    while Stack:
        currNode = stack.pop()
        Val.append(currNode.val)
        # print(currNode.val, end=' ')
    if currNode.left:
        Stack.append(currNode.left)
    if currNode.right:
        Stack.append(currNode.right)
    return Val
