class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=[]
        b=[]
        for i in nums:
            if i >0:
                a.append(i)
            else:
                b.append(i)
        c=[]
        for i in a:
            if -i in b:
                c.append(i)
        if len(c)==0:
             return -1
        else:
            return max(c)
        