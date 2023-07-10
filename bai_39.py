class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for num in candidates:
            for i in range(num, target + 1):
                for combination in dp[i - num]:
                    dp[i].append(combination + [num])
        return dp[target]