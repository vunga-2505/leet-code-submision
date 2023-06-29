class Solution:
    def isFascinating(self, n: int) -> bool:
        c = str(n)+str(2*n)+str(3*n)
        if '0' in c :
            return False
        if len(c)>9:
            return False
        for i in range(1,10):
            if str(i) not in c:
                return False
        return True