class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        a =[]
        for i in range(len(number)):
            if number[i] == digit:
               a.append(int(number[:i]+number[i+1:]))
        return str(max(a))