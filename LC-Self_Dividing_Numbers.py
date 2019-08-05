# # #   Self Dividing Numbers   # # #

# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
# and 128 % 8 == 0. Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible.

# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

class Solution:
    def selfDividingNumbers(self, left: int, right: int):

        # # # # #    Solution 1: idea     # # # # #
        #    1. Check each number between left and right bounds
        #    2. If it contains "0", skip
        #    3. If it is divisible of each of it's digit

        # Final list for storing the correct numbers
        # finalList = []
        # # 1st loop for all the numbers in [left,right]
        # for num in range(left, right+1):
        #     # Convert integer to string for iteration
        #     strNum = str(num)
        #     # If number only contains 1 digit, is correct
        #     if len(strNum) == 1:
        #         finalList.append(num)
        #         # print(finalList)
        #     else:
        #         if int(strNum[-1]) != 0:
        #             #print("2 digits: ", strNum)
        #             # 2nd loop for all the digits in the string form of the number
        #             count = 0
        #             for digit in strNum:
        #                 if int(digit) != 0 and int(strNum) % int(digit) == 0:
        #                     #print("strNum: ", strNum)
        #                     #print("digit: ", int(digit))
        #                     count += 1
        #             #print("count: ", count)
        #             if count == len(strNum):
        #                 finalList.append(int(strNum))
        # return finalList

        # # # # #    Solution 2: idea     # # # # #
        #   1. Define a self-division function return the correct number
        #   2. Check if each digit, if it contains "0" or % > 0 return false
        def self_div(num):
            snum = str(num)
            for d in snum:
                if d == "0" or num % int(d) > 0:
                    return False
            return True
        # Apply self_div function on each element
        ans = []
        for num in range(left, right+1):
            if self_div(num):
                ans.append(num)
        return ans

        # # # # #    Solution 2: Idea     # # # # #
        #   1. Function using Lambda
        #   2. Filter method return correct Numbers
        # is_self_div = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        # return filter(is_self_div, range(left,right+1))

t = Solution()
print(t.selfDividingNumbers(1, 22))
