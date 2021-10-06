#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        x_input = abs(x)
        if x >= 2 ** 31 - 1 or x <= -(2 ** 31):
            return 0
        else:
            while(x_input != 0):
                pop = x_input % 10
                x_input = x_input // 10
                rev = rev * 10 + pop
            if rev >= 2 ** 31 - 1 or rev <= -(2 ** 31):
                return 0 
            elif x < 0:
                return 0 - rev
            else:
                return rev
# @lc code=end

