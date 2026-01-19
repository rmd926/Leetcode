class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
                nums2.remove(num)
        return ans

# Runtime: 16 ms Beats 5.05 %
# Memory: 19.39 MB Beats 20.39 %

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums2)
        ans = []
        for x in nums1:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

# Runtime: 2 ms Beats 45.98 %
# Memory: 19.46 MB Beats 13.94 %
