class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for x in nums:
            ans += [cur + [x] for cur in ans]
        return ans

# Runtime: 0 ms 100.00 %
# Memory: 19.43 MB Beats 26.82 %
