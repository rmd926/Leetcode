class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while slow < fast and fast < len(nums):
            if nums[slow] != nums[fast]:
                return nums[slow]
            else:
                slow += 2 
                fast += 2
        
        return nums[-1]

# Runtime: 3 ms Beats 14.99 %
# Memory: 26.92 MB Beats 69.39 %
