
#
# [258] Add Digits
#

# @lc code=start
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sum=0
            while num>0:
                sum= sum+num%10
                num=num//10
            num =sum
        
        return num


        
# @lc code=end
        
# @lc code=end