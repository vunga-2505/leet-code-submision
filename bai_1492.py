class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        dem=0
        for i in range(1, n+1):
            if n%i==0:
                dem=dem+1
                if dem==k:
                    return i
        return -1