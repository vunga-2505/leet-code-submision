class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        
        a=[0,1,1]
        for i in range(3,n+1):
            an= a[i-3]+a[i-2]+a[i-1]
            a.append(an)
        return an
            