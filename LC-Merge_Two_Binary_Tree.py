# # # Merge Two Binary Trees # # #

# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:
#  Input:
# 	   Tree 1                   Tree 2
#             1                       2
#            / \                     / \
#           3   2                   1   3
#          /                         \   \
#         5                           4   7
#  Output:
#  Merged tree:
# 	                3
# 	               / \
# 	              4   5
# 	             / \   \
# 	            5   4   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):

        # # #     Solution      # # #
        # 1. Recursively add two nodes
        # If t1 and t2 exists
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

a1 = Tree = TreeNode(1)
b1 = Tree.left = TreeNode(3)
c1 = Tree.right = TreeNode(2)
d1 = Tree.left.left = TreeNode(5)

a2 = Tree = TreeNode(2)
b2 = Tree.left = TreeNode(1)
c2 = Tree.right = TreeNode(3)
d2 = Tree.left.right = TreeNode(4)
f2 = Tree.right.right = TreeNode(7)

t = Solution()
print(t.mergeTrees(a1, a2).left.right.val)
