class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]

# Runtime: 0 ms Beats 100.00 %
# Memory: 20.41 MB Beats 45.26 %
