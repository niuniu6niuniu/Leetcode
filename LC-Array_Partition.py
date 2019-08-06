# # #   Array Partition I   # # #

# Given an array of 2n integers, your task is to group these integers into n
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
# min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

class Solution:
    def arrayPairSum(self, nums):

        # # #   Solution 1   # # #
        #   1. Sort the list
        #   2. For loop recursively add items strp by 2
        n = len(nums) / 2
        end = int(n * 2)
        nums.sort()
        sum = 0
        for i in range(0, end, 2):
            sum += nums[i]
        return sum

        # # #   Solution 2   # # #
        #    1. Sort()
        #    2. Slicing
        nums.sort()
        return sum(nums[::2])

        # # #   Solution 3   # # #
        #   1. Sorted
        #   2. Slicing
        return sum(sorted(nums)[::2])

t = Solution()
print(t.arrayPairSum([1,4,3,2,5,6,8,7]))
