# Jewels and Stones
# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have. Each character in S is a type of
# stone you have. You want to know how many of the stones you have are also
# jewels. The letters in J are guaranteed distinct, and all characters in J
# and S are letters. Letters are case sensitive, so "a" is considered a different
# type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:
# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        # Solution 1: ------ Iteration ------
        # Idea: Cross check 2 list, if found, add 1 to count
        count = 0
        # Iterate through J and S
        for j in J:
            for i in range(len(S)):
                if S[i] == j:
                    count += 1
        return count

        # Solution 2: ------ replace() ------
        # Idea: Remove the jewels from stone list, check length
        lenFull = len(S)
        for j in J:
            S = S.replace(j, '')
        return lenFull - len(S)

        # Solution 3: ------ count ------
        # Idea: Use string.count() directly count jewels in stone list
        count = 0
        for j in J:
            count += S.count(j)
        return count

    num = numJewelsInStones(None, "aA", "aAAbbbb")
    print(num)
