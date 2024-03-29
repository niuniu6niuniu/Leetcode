# # #   Flipping Image # # #
# Given a binary matrix A, we want to flip the image horizontally, then
# invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced
# by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# Idea: 1. Reverse each row, use stack or slicing
#       2. Swap "0" and "1", use 2 for loops
class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            # Reverse list
            A[i] = A[i][::-1]
            # temp = []
            # while A[i]:
            #     m = A[i].pop()
            #     temp.append(m)
            # A[i] = temp
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
            return A

t = Solution()
A = [[1,1,0],[1,0,1],[0,0,0]]
print(t.flipAndInvertImage(A))
