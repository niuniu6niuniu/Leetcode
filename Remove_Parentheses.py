# Remove Outermost Parentheses
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not
# exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition:
# S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in
# the primitive decomposition of S.

# Example 1:
# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
#
# Example 2:
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
#
# Example 3:
# Input: "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # Solution 1: count
        reserveList = []
        count = 0
        for index, item in enumerate(S):
            if item == '(':
                count += 1
            if count > 1:
                reserveList.append(item)
            if item == ')':
                count -= 1
        return "".join(reserveList)

        # Solution 2: Stack
        stack = []
        ans = ""
        for i in range(len(S)):
            if S[i] == "(":
                if stack != []:
                    ans += S[i]
                stack.append(i)
            # if S[i] == ')'
            else:
                m = stack.pop()
                if stack != []:
                    ans += S[i]
        return ans

testCase = Solution()
print(testCase.removeOuterParentheses("(()(()))()"))
