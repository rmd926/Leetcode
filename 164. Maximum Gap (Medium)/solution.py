class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_gap = 0
        if len(nums) == 1:
            return 0
        
        for i in range(1, len(nums)):
            temp = nums[i] - nums[i-1]
            if temp > max_gap:
                max_gap = temp
                
        return max_gap
