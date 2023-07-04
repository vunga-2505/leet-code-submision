class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1) & set(nums2)
        if len(a)==0:
            return -1
        else:
            return min(a)