# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        return n == 1
# @lc code=end
