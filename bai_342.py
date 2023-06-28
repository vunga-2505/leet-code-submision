# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, n:int)->bool:
        b=n
        if b<=0:
            return False
        while True:
            if b==1:
                return True
            if b%4!=0:
                return False
            b=round(b/4)

# @lc code=end