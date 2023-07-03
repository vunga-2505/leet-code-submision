class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if 1 in nums:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i]:
                    if nums[i]  > 0:
                        return nums[i] + 1 
            return nums[len(nums) - 1] + 1 
        else:
            return 1 