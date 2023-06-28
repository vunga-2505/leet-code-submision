class Solution:
  def separateDigits(self, nums: List[int]) -> List[int]:
        r = []
        for x in nums:
            a = []
            while x > 0:
                 a.insert(0, x % 10)
                 x = x // 10
            r += a
        return r