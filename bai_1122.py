class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in arr2:
            for j in arr1:
                if j==i:
                    a.append(j)
        for num in arr1:
            if num not in arr2:
                b.append(num)
        b.sort()
        return a+b