class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a= str(n)
        sum = 0

        for i in range(len(a)):
            b= int(a[i])

            if i % 2 == 0:
                sum += b
            else:
                sum -= b

        return sum