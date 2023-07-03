#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        b=""
        n=abs(num)
        while n>=1:
            b+=str(n%7)
            n=n//7
        if num>0:
            return b[::-1]
        else:
            return '-'+b[::-1]

    

        
# @lc code=end

