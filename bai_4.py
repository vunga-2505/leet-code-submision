# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums =nums1+nums2
        nums.sort()
        n = len(nums)//2
        if len(nums)%2!=0:
            return nums[int(n)]
        else:
            return (nums[n]+nums[n-1])/2
        
        
# @lc code=end