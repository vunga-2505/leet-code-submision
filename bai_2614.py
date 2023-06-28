def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        return True

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxp=0
        
        for i in range(0,len(nums)):
            val1 = nums[i][i]
            if is_prime(val1) and val1>maxp:
                maxp = val1
            val2 = nums[i][len(nums)-i-1]
            if is_prime(val2) and val2>maxp:
                maxp = val2
        return maxp
        
            

       