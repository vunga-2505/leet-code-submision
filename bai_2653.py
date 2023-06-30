from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        L= SortedList()
        for i in range(k):
            L.add(nums[i])
            res = []
        if L[x - 1] < 0:
                res.append(L[x-1])
        else:
                res.append(0)
        for i in range(k, len(nums)):
            L.add(nums[i])
            L.discard(nums[i - k])
            
            if L[x - 1] < 0:
                res.append(L[x - 1])
            else:
                res.append(0)
        
        return res