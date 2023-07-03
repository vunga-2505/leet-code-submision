#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=[]  
        for i in nums:
            if i>0:
                a.append(i)
            else:
                b.append(i)  
        for j in range(len(a)):
            c.append(a[j])
            c.append(b[j])
        return c
# @lc code=end

