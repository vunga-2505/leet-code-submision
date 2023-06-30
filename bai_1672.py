class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=[]
        for i in range(0,(len(accounts))):
            sum=0
            for j in range(0,len(accounts[0])):
                sum+=accounts[i][j]
            a.append(sum)
        return max(a)