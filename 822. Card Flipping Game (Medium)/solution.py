# 所有出現在 fronts 或 backs 的數字中，且不屬於任何 fronts[i]==backs[i] 的數字，取最小值；若不存在回 0。
from collections import Counter
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad_num = set()
        for f, b in zip(fronts, backs):
            if f == b:
                bad_num.add(f)

        temp = []
        combine = fronts+backs

        for num in combine:
            if num not in bad_num:
                temp.append(num)
        
        return min(temp) if temp else 0

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.48 MB Beats 7.10 %
