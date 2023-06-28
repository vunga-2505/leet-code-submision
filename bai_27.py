class Solution(object):
  def removeElement(self, nums=list, val=int):
      i = 0
      a = []
      for j in range(len(nums)):
        if nums[j] == val:
            a.append(nums[j])
        else:
            nums[i] = nums[j]
            i += 1
      return i