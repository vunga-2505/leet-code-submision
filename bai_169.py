# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        n = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                n= i
            if n == i:
                count += 1
            else:
                count -= 1
        return n

        
# @lc code=end