# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = []
        for i in range(0,len(nums)):
            if nums[i] != 0:
                a.append(nums[i])
        a += [0] * (len(nums) - len(a))
        for i in range(0,len(nums)):
            nums[i] = a[i]
# @lc code=end
