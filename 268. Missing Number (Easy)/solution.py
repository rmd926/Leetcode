'''
數學公式解(Optimal):
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        gt = (n * (n + 1)) // 2
        temp = sum(nums)
        return gt - temp

'''
排序法: 
Time Complexity: O(nlogn)
Space Complexity: O(n) or O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
          
        elif nums[-1] != len(nums):
            return len(nums)
          
        else:
            for i in range(0, len(nums)-1):
                if nums[i+1] - nums[i] != 1:
                    return nums[i] + 1
