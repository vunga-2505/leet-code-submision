class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum = {}
        for num1 in nums1:
            for num2 in nums2:
                p = num1 + num2
                if p in sum:
                    sum[p] += 1
                else:
                    sum[p] = 1
        for num3 in nums3:
            for num4 in nums4:
                t = -(num3 + num4)
                if t in sum:
                    count += sum[t]

        return count