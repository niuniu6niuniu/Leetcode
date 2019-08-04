# # #   Sort Array By Parity   # # #
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Idea: 1. Create a empty list B = []
#       2. check the elements one by one, if it is even, append
class Solution:
    def sortArrayByParity(self, A):
        B = []
        for itemE in A:
            if itemE % 2 == 0:
                B.append(itemE)
        for itemO in A:
            if itemO % 2 == 1:
                B.append(itemO)
        return B

    # Solution 2: List sort using keywords
    # A.sort(key = lambda x: x % 2)

    # Solution 3: List = sub-list + sub-list
    #  return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])

t = Solution()
print(t.sortArrayByParity([3,1,2,4,3,6]))
