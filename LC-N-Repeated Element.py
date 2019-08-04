# # #   N-Repeated Element in Size 2N Array   # # #
import random
# In a array A of size 2N, there are N+1 unique elements, and exactly one of
# these elements is repeated N times. Return the element repeated N times.
# Example 1:
# Input: [1,2,3,3]
# Output: 3

# Example 2:
# Input: [2,1,2,5,3,2]
# Output: 2

# Example 3:
# Input: [5,1,5,2,5,3,5,4]
# Output: 5

# Idea: 1. Create a new list
#       2. Recursively add elements to the new list from the given one
#       3. If find the element was already in the new list, return
class Solution:
    def repeatedNTimes(self, A):
        # Solution 1:
        # Idea: Create an empty list
        #       Recursively add elements to the list from the given one
        #       If find the repeated element, return
        # cklist = []
        # for item in A:
        #     if item not in cklist:
        #         cklist.append(item)
        #     else:
        #         foundItem = item
        # return foundItem

        # Solution 2:
        # Idea: check each element, use cound() method
        # for item in A:
        #     if A.count(item) > 1:
        #         return item

        # Solution 3:
        # Idea: Random sampling
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]

t = Solution()
print(t.repeatedNTimes([5,1,5,2,5,3,5,4]))
