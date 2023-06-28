class Solution(object):
    def heightChecker(self, heights):
        e = sorted(heights)
        dem =0
        for i in range (len(heights)):
            if heights[i] != e[i] :
                dem= dem+1
        return dem
        