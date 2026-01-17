class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = max(nums)
        return nums.index(max_num)

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.55 MB Beats 7.99 %
