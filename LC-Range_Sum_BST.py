# Range Sum of BST
# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).The binary search tree is guaranteed
# to have unique values.

# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        # Solution 1: ------ Stack Iterative ------
        # Idea: 1. push root in stack, check if L < root.val < R and then add root.val to count
        #       2. if root.cal > L(root.val !< L), then push root.left in stack ready for check
        #       3. if root.val < R(root.val !> R), then push root.right in stack ready for check
        count = 0
        stack = [root]
        while stack:
          node = stack.pop()
          # if node is not null
          if node:
               if L <= node.val <= R:
                    count += node.val
               if node.val > L:
                    stack.append(node.left)
               if node.val < R:
                    stack.append(node.right)
        return count

        # Solution 2: ------ DFS, Recursive ------
        # Idea: 1. Start from root, check if L < root.val < R then add root.val to count
        #       2. If root.val > L(root.val !< L), check for root.left 
        #       3. If root.val < R(root.val !> R), check for root.right
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                # If current node.val < L
                # Useless to explore the left subtree
                if node.val > L:
                    dfs(node.left)
                # If the current node.val > #
                # Useless to explore the right subtree
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
