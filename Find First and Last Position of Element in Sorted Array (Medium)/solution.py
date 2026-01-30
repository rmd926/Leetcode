class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def Find_First(nums, target):
            left = 0
            right = len(nums) - 1
            #mid == nums[(left+right) // 2]
            while left <= right:
                mid = (left+right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid 
                    right = mid - 1
            return -1
        
        def Find_Last(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1
            return -1

        first = Find_First(nums, target)
        if first == -1:
            return [-1, -1]
        else:
            last = Find_Last(nums, target)
            return [first, last]        
