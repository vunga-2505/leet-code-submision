class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=[]
        for i in nums:
            a.append(int(i))
        b= sorted(a,reverse=True)
        return str(b[k-1])