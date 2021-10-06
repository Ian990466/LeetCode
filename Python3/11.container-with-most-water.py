#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = min(height[left],height[right]) * right
        
        for i in range(len(height)-2):
            if height[left] > height[right]:
                right -= 1
                area = min(height[left],height[right]) * (right-left)
                if area > max_area:
                    max_area = area
            else:
                left += 1
                area = min(height[left],height[right]) * (right-left)
                if area > max_area:
                    max_area = area

        return max_area

# @lc code=end

