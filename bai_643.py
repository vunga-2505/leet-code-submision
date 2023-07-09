class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a=[]
        for i in range(0,len(nums)):
            if i <k:
                a.append(nums[i])
        b= sum(a)
        c = b
        for i in range(k, len(nums)):
            c =c+ nums[i] - nums[i-k]
            b = max(b, c)
        return b / k