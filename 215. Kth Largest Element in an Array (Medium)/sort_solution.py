class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# Runtime: 51 ms Beats 84.54 %
# Memory: 31.13 MB Beats 23.83 %
