#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        atoi = 0
        positive = True
        flag = False
        # s = s.replace(" ", "")
        for c in range(len(s)):
            if flag == False:
                if s[c] == '-':
                    flag = True
                    positive = False
                elif s[c] == '+':
                    flag = True
                    positive = True
                elif s[c] == " ":
                    continue
                elif s[c] in number:
                    flag = True
                    for i in range(len(number)):
                        if s[c] == number[i]:
                            atoi = atoi * 10 + i
                else:
                    return 0
            elif flag == True:
                if s[c] in number:
                    buffer = False
                    for i in range(len(number)):
                        if s[c] == number[i]:
                            buffer = True
                            atoi = atoi * 10 + i
                    flag = flag and buffer
                else:
                    break
            
                    

        if positive == False:
            if atoi > 2 ** 31:
                return 0 - 2 ** 31
            else:
                return 0 - atoi
        else:
            if atoi > 2 ** 31 - 1:
                return 2 ** 31 -1
            else:
                return atoi
# @lc code=end

