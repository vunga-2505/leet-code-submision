# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        a=sorted(s)
        b=sorted(t)
        flag=0
        for i in range(len(a)):
            if(a[i]!=b[i]):
                flag=1
                break
        if(flag==0):
            return True
        else:
            return False
        
# @lc code=end