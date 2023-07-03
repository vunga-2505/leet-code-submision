#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) %2 !=0:
           return False
        for i in nums:
            if nums.count(i)%2!=0:
                return False
        return True
        
        
# @lc code=end

