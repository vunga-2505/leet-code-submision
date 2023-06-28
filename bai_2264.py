class Solution:
    def largestGoodInteger(self, num: str) -> str:
        r=''
        c =1
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                c+=1
            else :
                c=1
            if c==3:
                r =max(r,num[i]*3)
        return r