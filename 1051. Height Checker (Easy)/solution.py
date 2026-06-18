class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        gt = sorted(heights)
        n = len(gt)

        count = 0
        for i in range(n):
            if heights[i] != gt[i]:
                count += 1
        
        return count

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.23 MB Beats 53.66 %
