class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for p in range(len(nums)):
            if left == total - nums[p] - left:
                return p
            else:
                left += nums[p]

        return -1
# Runtime: 7 ms Beats 57.74 %
# Memory: 20.42 MB Beats 9.17 %
