class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)-1):
            if  nums[i] != nums[0] and nums[i] != nums[-1]:
                return nums[i]
        return -1