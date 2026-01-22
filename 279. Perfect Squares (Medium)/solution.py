class Solution:
    def numSquares(self, n: int) -> int:
        square_list = [int(i**2) for i in range(1, 101)]
        dp = [0] + [float("inf")] * n

        for i in range(1, n+1):
            for sq in square_list:
                if sq > i:
                    break
                dp[i] = min(dp[i-sq] + 1, dp[i])
        
        return dp[n]

# Runtime: 1335 ms Beats 81.16 %
# Memory: 19.57 MB Beats 30.02 %
