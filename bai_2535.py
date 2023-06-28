class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = 0
        for num in nums:
            i = num
            while i > 0:
                d = i % 10
                sum2 += d
                i //= 10
        return abs(sum1 - sum2)