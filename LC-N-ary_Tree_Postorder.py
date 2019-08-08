# # #   N-ary Tree Postorder Traversal   # # #

# Given an n-ary tree, return the postorder traversal of its nodes' values.
# For example, given a 3-ary tree:
#          1
#        / | \
#       3  2  4
#      / \
#     5   6
# Return its postorder traversal as: [5,6,3,2,4,1].

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):

        # # #   Recursion   # # #
        ans = []
        if root == None:
            return ans

        def recursion(root, ans):
            for child in root.children:
                recursion(child, ans)
            ans.append(root.val)

        recursion(root, ans)
        return ans
        # # #   Recursion   # # #

        # # #   Iteration   # # #
        ans = []
        if root == None:
            return ans
        # Initialize stack
        stack = [root]
        while stack:
            currentNode = stack.pop()
            ans.append(currentNode.val)
            stack.extend(currentNode.children)
        # Reverse order
        return ans[::-1]
        # # #   Iteration   # # #
