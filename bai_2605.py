class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
    
        i = 0
        j = 0
    
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        min1 = 10 * nums1[0] + nums2[0]
        min2 = 10 * nums2[0] + nums1[0]

    
        return min(min1,min2)