class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
    
    
        for i in range(1, len(nums)):
            result &= set(nums[i])
        result = list(result)
        result.sort()
    
        return result