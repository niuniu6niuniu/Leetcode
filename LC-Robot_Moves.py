# # #   Robot Return to Origin   # # #

# There is a robot starting at position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0)
# after it completes its moves.
# The move sequence is represented by a string, and the character moves[i]
# represents its ith move. Valid moves are R (right), L (left), U (up), and
# D (down). If the robot returns to the origin after it finishes all
# of its moves, return true. Otherwise, return false.

# Example 1:
# Input: "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the
# same magnitude, so it ended up at the origin where it started. Therefore, we
# return true.

# Example 2:
# Input: "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left
# of the origin. We return false because it is not at the origin at the end of
# its moves.

# Idea: 1. Check each letter in the moves string
#       2. Up: +2, Down: -2, Left: -1, Right: +1
class Solution:
    def judgeCircle(self, moves):
        count = 0
        for move in moves:
            if move == "U":
                count += 2
            elif move == "D":
                count -= 2
            elif move == "L":
                count -= 1
            else:
                count += 1
        if count == 0:
            return True
        else:
            return False

t = Solution()
moves = "UDRL"
print(t.judgeCircle(moves))
