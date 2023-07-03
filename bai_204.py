#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False
        return sum(prime)
# @lc code=end

