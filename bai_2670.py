class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            p = len(set(nums[:i+1]))
            s = len(set(nums[i+1:]))
            a.append(p-s)
        return a