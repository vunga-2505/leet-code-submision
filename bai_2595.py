class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n)[2:] 
        a= 0
        c = 0

        for i, bit in enumerate(reversed(b)):
            if bit == '1':
                if i % 2 == 0:
                    a+= 1
                else:
                    c+= 1

        return [a, c]