class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        maxs = 0

        for i in range(0, len(nums), 2):
            maxs += nums[i]

        return maxs