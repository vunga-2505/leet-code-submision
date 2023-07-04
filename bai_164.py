class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        a=[]
        for i in range(0,len(nums)-1):
            b= (nums[i+1]-nums[i])
            a.append(b)
        return max(a)
        