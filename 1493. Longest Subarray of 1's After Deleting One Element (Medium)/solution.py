class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        num_zero = 0
        max_length = 0
        left = 0

        for right in range(n):
            if nums[right] == 0:
                num_zero += 1
            
            while num_zero > 1:
                if nums[left] == 0:
                    num_zero -= 1
                left += 1
            
            max_length = max(max_length, right - left) # 因為不論是否為0，都要刪除一格
        
        return max_length
