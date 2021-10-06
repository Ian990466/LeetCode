#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in output:
                output[num] = i
            else:
                return [output[n], i]
# @lc code=end

