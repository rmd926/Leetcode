class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        target = sorted(nums)
        ans = []
        for num in nums:
            ans.append(target.index(num))
            
        return ans

# Runtime: 15 ms Beats 54.15 %
# Memory: 19.21 MB Beats 12.10 %
