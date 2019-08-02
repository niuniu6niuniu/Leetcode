# To Lower Case
# Implement function ToLowerCase() that has a string parameter str,
# and returns the same string in lowercase.

# Example 1:
# Input: "Hello"
# Output: "hello"
# Example 2:
# Input: "here"
# Output: "here"
# Example 3:
# Input: "LOVELY"
# Output: "lovely"

# Keywords: ------ replace ------
# Idea: check each item in the string, replace it with it's lower case
class Solution:
    def toLowerCase(self, str: str) -> str:
        for word in str:
            str = str.replace(word, word.lower())
        return str

lowStr = Solution()
print(lowStr.toLowerCase("HELLO"))
