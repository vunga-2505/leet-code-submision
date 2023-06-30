class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)

        c= 0
        for i in range(k):
            c+=m
            m+=1
        return c

        