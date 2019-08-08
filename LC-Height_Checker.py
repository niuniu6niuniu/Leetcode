# # #     Height Checker     # # #

# Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students not standing in the right positions.
# (This is the number of students that must move in order for all students to be
# standing in non-decreasing order of height.)

# Example 1:
# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation:
# Students with heights 4, 3 and the last 1 are not standing in the right positions.

class Solution:
    def heightChecker(self, heights):
        # # #   Solution 1  # # #
        sortH = sorted(heights)
        print(sortH)
        count = 0
        for i in range(len(heights)):
            if sortH[i] != heights[i]:
                count += 1
        return count

        # # #   Solution 2   # # #
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

t = Solution()
h = [7,4,5,6,4,2,1,4,6,5,4,8,3,1,8,2,7,6,3,2]
print(t.heightChecker(h))
