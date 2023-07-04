class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        dem = Counter(nums)
        dem2 = 0
        for num in dem:
            if k == 0:
                if dem[num] > 1:
                    dem2 += 1
            else:
                if num + k in dem:
                    dem2 += 1
        return dem2