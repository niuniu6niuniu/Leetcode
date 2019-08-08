# # #     Search in Binary Tree     # # #

# Given the root node of a binary search tree (BST) and a value. You need to find
# the node in the BST that the node's value equals the given value. Return the
# subtree rooted with that node. If such node doesn't exist, you should return NULL.

# For example,
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# And the value to search: 2
# You should return this subtree:
#
#       2
#      / \
#     1   3
# In the example above, if we want to search the value 5, since there is no node
# with value 5, we should return NULL.
# Note that an empty tree is represented by NULL, therefore you would see the
# expected output (serialized tree format) as [], not null.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):

        # # #   Solution 1  # # #
        # val is smaller than root, search the sub-left tree
        if root and root.val > val:
            return self.searchBST(root.left, val)
        # val is greater than root, search the sub-right tree
        elif root and root.val < val:
            return self.searchBST(root.right, val)
        # val is equal to root, return root
        return root

        # # #   Solution 2   # # #
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left        

a = Tree = TreeNode(4)
b = Tree.left = TreeNode(2)
c = Tree.right = TreeNode(7)
d = Tree.left.left = TreeNode(1)
e = Tree.left.right = TreeNode(3)

t = Solution()
print(t.searchBST(a, 2).val)
