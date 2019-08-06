# # #   DI String Match   # # #

# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
# 1. If S[i] == "I", then A[i] < A[i+1]
# 2. If S[i] == "D", then A[i] > A[i+1]

# Example 1:
# Input: "IDID"
# Output: [0,4,1,3,2]
#
# Example 2:
# Input: "III"
# Output: [0,1,2,3]
#
# Example 3:
# Input: "DDI"
# Output: [3,2,0,1]

class Solution:
    def diStringMatch(self, S: str):

        # # #    Solution 1   # # #
        #   1. Iterate the sting S, check it is "I" or "D"
        #   2. Set a low pointer and high pointer, if it is "I", append low,
        #      if it is "D", append high. To make sure increase of decrease
        #      between "I" and "D"
        #   3. At the end of each iteration, low plus 1, hight minus 1, to make
        #      sure increase between "I" and "I" or decrease betwee "D" and "D"
        #   4. Finally low meets high, append either one of them
        ans = []
        lo = 0
        hi = len(S)
        for x in S:
            if x =="I":
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        return ans + [lo]


t = Solution()
print(t.diStringMatch("IDID"))
