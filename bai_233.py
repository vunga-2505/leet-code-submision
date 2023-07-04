class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        a = 1  
        
        while a <= n:
            b = n // (a * 10)
            c = n % (a * 10)
            count += b * a
            e = c // a
            if e == 1:
                count += c % a + 1
            elif e > 1:
                count += a
            a *= 10
        
        return count