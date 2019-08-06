# # #    Peak Index in a Mountain Array   # # #

# Let's call an array A a mountain if the following properties hold:
# 1. A.length >= 3
# 2. There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1]
#    < A[i] > A[i+1] > ... > A[A.length - 1]

# Given an array that is definitely a mountain, return any i such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:
# Input: [0,1,0]
# Output: 1

# Example 2:
# Input: [0,2,1,0]
# Output: 1

class Solution:
    def peakIndexInMountainArray(self, A):

        # # #    Solution 1 # # #
        #   1. Iterate  the list, find the element that all the elements on
        #       it's left smaller and all the elements on the it's right bigger
        #   2. Define 2 functions, check elements on the left and right
        # def left_ck(A, i):
        #     for m in range(i):
        #         if A[m] >= A[i]:
        #             return False
        #     return True
        #
        # def right_ck(A, i):
        #     for n in range(i+1, len(A)):
        #         if A[i] <= A[n]:
        #             return False
        #     return True
        #
        # for i in range(1, len(A)-1):
        #     if left_ck(A, i) and right_ck(A, i):
        #         return i

        # # #   Solution 2    # # #
        #   1. Return the index of the max element in the list
        # return A.index(max(A))

        # # #   Solution 3   # # #
        #   1. One side check, climb from the left bottom and stop when reach the top
        # i = 0
        # while i < len(A):
        #     if A[i] < A[i+1]:
        #         i += 1
        #     else:
        #         return i

        # # #   Solution 4   # # #
        # # #  Binary Search  # # #
        left = 0
        right = len(A)-1
        while left < right:
            mid = (left + right) // 2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            # if A[mid] is left of the top, move towards right
            elif A[mid] < A[mid+1]:
                left = mid
            # if A[mid] is right of the top, move towards left
            else:
                right = mid

t = Solution()
print(t.peakIndexInMountainArray([0,2,1]))
