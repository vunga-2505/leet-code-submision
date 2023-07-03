#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        for j in range(0,len(a)):
            c.append(a[j])
            c.append(b[j])
        return c
            
        
# @lc code=end

