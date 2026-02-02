class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(num % 2)

        return sorted(ans)

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.55 MB Beats 28.42 %
