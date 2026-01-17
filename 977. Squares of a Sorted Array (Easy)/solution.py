class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = int(nums[i] ** 2)
        return sorted(nums)

# Runtime: 3 ms Beats 95.91 %
# Memory: 20.64 MB Beats 18.18 %
