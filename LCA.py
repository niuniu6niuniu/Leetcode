# Lowest Common Ancestor
# For two givens nodes A an B, look for the lowest common ancestor

# Initiate Tree
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution():
    def LCA(self, root, A, B):
        # if empty tree or A is root or B is root
        if root is None or root == A or root == B:
            return root
        else:
            # search left subtree
            L = self.LCA(root.left, A, B)
            # search right subtree
            R = self.LCA(root.right, A, B)
            # if find A and B
            if L and R:
                return root
            elif not L:
                return R
            else:
                return L

# Root
a = Tree = TreeNode(10)
b = Tree.left = TreeNode(5)
c = Tree.right = TreeNode(15)
d = Tree.left.left = TreeNode(3)
e = Tree.left.right = TreeNode(7)
f = Tree.right.left = TreeNode(None)
h = Tree.right.right = TreeNode(18)
testCase = Solution()
print(testCase.LCA(a, d, e).val)
