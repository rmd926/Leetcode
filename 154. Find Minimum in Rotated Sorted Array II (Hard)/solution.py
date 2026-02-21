class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (right + left) // 2
            # 如果中位數>右邊的值，代表target在右半邊
            if nums[mid] > nums[right]:
                left = mid + 1

            # 如果中位數<右邊的值，代表target在左半邊
            elif nums[mid] < nums[right]:
                right = mid
            
            else: # 因為需要考慮重複的值，所以把right pointer往左邊縮減
                right -= 1
        
        return nums[left]
