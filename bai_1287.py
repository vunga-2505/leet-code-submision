class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        b=[]
        for i in arr:
            a=arr.count(i)
            b.append(a)
        for j in arr:
            if arr.count(j)==max(b):
                return j