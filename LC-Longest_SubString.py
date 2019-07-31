# Given a string, find the length of the longest substring
# without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Idea: 1. Get all the non-repeated sub-string
#       2. Return the substirng with max length using "key"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return(0)
        else:
            strList = []
            for p in range(len(s)):
                strList.append(s[p])
                for q in range(p+1, len(s)):
                    if s[q] in s[p:q]:
                        break
                    else:
                        strList.append(s[p:q+1])
                        
            # Print out the string with max length 
            maxList = max(strList, key=len)
            return(len(maxList))
