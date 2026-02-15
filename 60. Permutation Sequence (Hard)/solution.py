import itertools
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n+1)]
        count = 0

        for perm in itertools.permutations(digits):
            count += 1
            if count == k:
                return "".join(perm)

# Runtime: 427 ms Beats 13.82 %
# Memory: 19.40 MB Beats 61.49 %
