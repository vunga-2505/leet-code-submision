class Solution:
    def averageValue(self, nums: List[int]) -> int:
        dem=0
        sum=0
        for i in nums:
            if i%2==0 and i%3==0:
                dem = dem+1
                sum = sum+i
        if dem==0:
            return 0
        
        return int(sum/dem)

