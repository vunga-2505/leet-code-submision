#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        a = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in a:
                return [a[c], i]
            a[nums[i]] = i
        
# @lc code=end
