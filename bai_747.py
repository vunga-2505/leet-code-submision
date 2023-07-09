class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        b= sorted(nums)
        if b[len(b)-1]>= 2*b[len(b)-2]:
            for i in range(len(nums)):
                if nums[i] == b[len(b)-1]:
                    return i
        else:
            return -1