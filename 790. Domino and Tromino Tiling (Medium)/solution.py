class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n+1)
        if n < 2:
            return 1
        
        elif n >= 2:
            dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n+1):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % (10**9+7)
        
        return dp[n]

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.36 MB Beats 60.59 %
