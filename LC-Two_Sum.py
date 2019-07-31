# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Idea: Double for loop, iterate the array, check every pair
# Solution 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]

# Idea: Dictionary with .get() method
# Solution 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [_dict.get(target - m), i]
            _dict[m] = i
