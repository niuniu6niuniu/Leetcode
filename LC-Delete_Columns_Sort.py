# # #     Delete Columns to Make Sorted     # # #

# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete
# all the characters in those indices.
#
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices
# {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the
# remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
# (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)
#
# Suppose we chose a set of deletion indices D such that after deletions,
# each remaining column in A is in non-decreasing sorted order.
# Return the minimum possible value of D.length.

# Example 1:
# Input: ["cba","daf","ghi"]
# Output: 1
# Explanation:
# After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
# If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
#
# Example 2:
# Input: ["a","b"]
# Output: 0
# Explanation: D = {}
#
# Example 3:
# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation: D = {0, 1, 2}

class Solution:
    def minDeletionSize(self, A):

        # # #   Solution 1   # # #
        # 1. Iterate each column of each string, check if it is in non-decreasing order
        # 2. If it is in decreasing order, take the index of columns, append to "D"
        D = set()
        strLen = len(A[0])
        for i in range(strLen):
            columnCK = []
            for str in A:
                columnCK.append(str[i])
            if columnCK != sorted(columnCK):
                D.add(i)
        return len(D)

        # # #   Solution 2   # # #
        # 1. Using zip() to pair elements in each sub-string
        # 2. Using any() to check if it is non-decreasing
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col)-1)):
                ans += 1
        return ans

        # # #   Solution 3   # # #
        return sum(list(col) != sorted(col) for col in zip(*A))


t = Solution()
A = ["zyx","wvu","tsr"]
print(t.minDeletionSize(A))
