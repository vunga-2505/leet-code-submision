class Solution:
    def trimMean(self, arr: List[int]) -> float:
        a = []
        if len(arr) >= 2:
            arr.sort()
            num_to_remove = int(len(arr) * 0.05)
            a = arr[num_to_remove:len(arr)-num_to_remove]
            return sum(a)/len(a)