class Solution:
    def hammingWeight(self, n: int) -> int:
        dem=0
        while n != 0:
            if n & 1 == 1:
                dem += 1
            n = n >> 1
        return dem