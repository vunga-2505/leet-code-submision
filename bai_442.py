class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        b= set()
        for i in nums:
            n= len(b)
            b.add(i)
            if n==len(b):
                a.append(i)
        return a