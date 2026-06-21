class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for odd_index in range(1, len(nums), 2):
            ans -= nums[odd_index]
        for even_index in range(0, len(nums), 2):
            ans += nums[even_index]
        
        return ans

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.26 MB Beats 53.47 %
