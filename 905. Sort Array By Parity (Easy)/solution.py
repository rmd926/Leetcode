class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1 # 有互換才把左指針往右挪一格

        return nums

# Runtime: 3 ms Beats 48.48 %
# Memory: 20.00 MB Beats 8.91 %
