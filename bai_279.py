import math

def isPerfectSquare(num):
    sqrt = int(math.sqrt(num))
    return sqrt * sqrt == num
class Solution:
    def numSquares(self, n: int) -> int:
        d = [float('inf')] * (n + 1)
        d[0] = 0

        for i in range(1, n + 1):
            if isPerfectSquare(i):
                d[i] = 1
            else:
                j = 1
                while j * j <= i:
                    d[i] = min(d[i], d[i - j*j] + 1)
                    j += 1

        return d[n]