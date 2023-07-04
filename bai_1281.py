class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        b=[]
        a=str(n)
        for i in a:
            b.append(int(i))
        m=1
        for j in b:
            m=m*j
        return m-sum(b)


        