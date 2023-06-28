class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums.append(0)
        res, n = 0, 0
        for i in nums:
            if i!=0: n+=1
            else:
                res = max(n,res)
                n=0
        return res