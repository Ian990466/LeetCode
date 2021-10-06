#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal_num = False
        if x > (2 ** 31) - 1 or x < -(2 ** 31):
            return False
        else:
            x = str(x)
            num_len = len(x)
            if num_len == 1:
                return True
            for i in range(num_len // 2):
                if x[i] == x[-(i+1)]:
                    pal_num = True
                else:
                    return False
            return pal_num
# @lc code=end

