import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        target = [x for x in range(1, n+1)]
        ans = []
        for i in itertools.combinations(target, k):
            ans.append(i)
        return ans

# Runtime: 16 ms Beats 98.28 %
# Memory: 58.65 MB Beats 98.73 %
