class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n

        for i in range(2, n):
            if nums[i-2] - nums[i-1] == nums[i-1] - nums[i]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)

        # n = [1,3,5,8,9,10,11] 

        # n[0] - n[1] == n[1] - n[2]
        # n[i-2] - n[i-1] == n[i-1] - n[i]

        # dp[i] = dp[i-1] + 1

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.59 MB Beats 16.08 %
