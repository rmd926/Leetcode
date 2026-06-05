class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = 0
        num_zero = 0
        left = 0

        for right in range(n):
            if nums[right] == 0:
                num_zero += 1
            
            while num_zero > k:
                if nums[left] == 0:
                    num_zero -= 1
                left += 1 # 如果該sliding windows內超過k個0，且nums[left]是0，就把左邊的ptr往右挪

            temp_length = right - left + 1
            max_length = max(max_length, temp_length)

        return max_length

# Runtime: 59 ms Beats 61.74 %
# Memory: 22.02 MB Beats 85.00 %
