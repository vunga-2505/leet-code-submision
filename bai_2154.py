class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        for i in nums:
            if original in nums:
                original=2*original
        return original