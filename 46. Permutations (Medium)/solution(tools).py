import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in itertools.permutations(nums)]

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.54 MB Beats 39.35 %
