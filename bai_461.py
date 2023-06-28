class Solution(object):
    def hammingDistance(self, x, y):
         return bin(x^y)[2:].count("1")
