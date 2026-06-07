class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)
        coins.sort()

        for i in range(1, amount + 1):
            ans = float('inf')
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                
                ans = min(ans, dp[i-c] + 1)
            
            dp[i] = ans
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

# Runtime: 573 ms Beats 41.25 %
# Memory: 19.52 MB Beats 77.62 %
