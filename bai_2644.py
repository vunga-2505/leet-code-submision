class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        a=[]
        divisors.sort()
        for i in divisors:
            dem=0
            for j in nums:
                if j%i==0:
                    dem+=1
            a.append(dem)
        return divisors[a.index(max(a))]