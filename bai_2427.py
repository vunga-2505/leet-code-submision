class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        dem =0
        x= min(a,b)+1
        for i in range(1,x):
            if a%i==0 and b%i==0:
                dem=dem+1
        return dem