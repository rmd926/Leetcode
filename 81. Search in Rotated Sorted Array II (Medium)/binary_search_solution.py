class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in nums
        nums.sort()
        mid = len(nums) // 2
        left, right = 0, len(nums) - 1

        while left <= right:
            if target < nums[mid]:
                right = mid - 1
                mid = (left + right) // 2
            elif target > nums[mid]:
                left = mid + 1
                mid = (left + right) // 2
            else:
                return True
        
        return False

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.58 MB Beats 58.28 %
