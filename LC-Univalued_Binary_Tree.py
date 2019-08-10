# # #     Univalued Binary Tree     # # #

# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Example 1:
#
#        1
#       / \
#      1   1
#     / \   \
#    1   1   1
#
# Input: [1,1,1,1,1,null,1]
# Output: true
#
# Example 2:
#
#        2
#       / \
#      2   2
#     / \
#    5   2
#
# Input: [2,2,2,5,2]
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isUnivalTree(self, root):

        # # #   Recursive   # # #
        if not root:
             return

        if root.left:
            if root.left.val != root.val:
                return False

        if root.right:
            if root.right.val != root.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        # # #   Recursive   # # #

        # # #   DFS:   # # #
        # vals = []
        # # Recursively append each node's value
        # def dfs(node):
        #     # if node is not None
        #     if node:
        #         vals.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        #
        # dfs(root)
        # Unik = set(vals)
        # Unik.remove(None)
        # return len(Unik) == 1
        # # #   DFS   # # #

        # # #   Recursive 1 line   # # #
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)
        # # #   Recursive for fun   # # #

a = Tree = TreeNode(1)
b = Tree.left = TreeNode(1)
c = Tree.right = TreeNode(1)
d = Tree.left.left = TreeNode(1)
e = Tree.left.right = TreeNode(2)
f = Tree.right.left = TreeNode(None)
h = Tree.right.right = TreeNode(1)
t = Solution()
print(t.isUnivalTree(a))
