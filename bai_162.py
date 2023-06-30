class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if nums[i]==max(nums):
                return i