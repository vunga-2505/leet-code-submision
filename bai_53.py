class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_s = max_s = nums[0]
        for i in range(1, len(nums)):
            current_s = max(nums[i], current_s + nums[i])
            max_s = max(max_s, current_s)
        return max_s