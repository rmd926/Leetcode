class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        slow = 0
        fast = len(nums) - 1
        count = 0

        while slow < fast:
            if nums[slow] + nums[fast] < target:
                count += (fast - slow)
                slow += 1
                # fast = len(nums) -1
            
            elif nums[slow] + nums[fast] >= target:
                fast -= 1
            
        return count

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.42 MB Beats 6.99 %
