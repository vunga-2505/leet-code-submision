class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a= []
        for i in range(n):
            s1 = sum(nums[:i])
            s2 = sum(nums[i+1:])
            a.append(abs(s1- s2))
        return a