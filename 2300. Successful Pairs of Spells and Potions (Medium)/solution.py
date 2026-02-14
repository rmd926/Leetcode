from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for s in spells:
            l, r = 0, len(potions)
            while l < r:
                mid = (l + r) // 2
                if s * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            ans.append(len(potions) - l)

        return ans

# Runtime: 707 ms Beats 44.55 %
# Memory: 45.00 MB Beats 55.04 %
