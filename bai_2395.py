class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        b=set()
        for i in range(0, len(nums)-1):
            a=nums[i]+nums[i+1]
            if a in b:
                return True
            else:
                b.add(a)
        return False
            