class Solution:
    def trailingZeroes(self, n: int) -> int:
        a = 1
        for i in range(n, 0, -1):
            a *= i

        dem = 0
        while a % 10 == 0:
            dem += 1
            a //= 10
        
        return dem