# # #   N-ary Tree Preorder Traversal   # # #

# Given an n-ary tree, return the preorder traversal of its nodes' values.
# For example, given a 3-ary tree:
#          1
#        / | \
#       3  2  4
#      / \
#     5   6
# Return its preorder traversal as: [1,3,5,6,2,4].

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        # # #   Recursion   # # #
        ans = []
        if root == None:
            return ans

        def recursion(root, ans):
            ans.append(root.val)
            for child in root.children:
                ans.append(child.val)
                recursion(child, ans)

        recursion(root, ans)
        return ans
        # # #   Recursion   # # #

        # # #   Iteration   # # #
        ans = []
        if root == None:
            return ans

        stack = [root]
        while stack:
            currentNode = stack.pop()
            ans.append(currentNode.val)
            stack.extend(currentNode.children[::-1])
        return ans
        # # #   Iteration   # # #
