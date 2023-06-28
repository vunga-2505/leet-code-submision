class Solution(object):
    def isPalindrome(self, x):
        sum = 0
        n = x
        while n > 0:
            temp = n % 10
            sum = sum * 10 + temp
            n = n / 10
        if sum == x:
            return True
        else:
            return False