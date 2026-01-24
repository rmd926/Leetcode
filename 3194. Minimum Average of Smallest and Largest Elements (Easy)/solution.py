class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        min_avg = float("inf")
        left, right = 0, len(nums) - 1

        while left < right:
            temp = (nums[left] + nums[right]) / 2
            if temp < min_avg:
                min_avg = temp
            left += 1
            right -= 1
        
        return min_avg

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.41 MB Beats 15.44 %
