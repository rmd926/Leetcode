'''
本題必須要in-place修改！因此不允許:
建立一個新的list，然後使用set()並且把元素搬到新的list內，再取len()。
只能夠使用two pointer解。
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # 先建立快慢指針 slow = 0; fast = 1
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]: # 如果相同數字，則先把快指針往下一格
                continue
            elif nums[fast] != nums[slow]: # 如果有快慢指針分別指向不同的數字，則先把慢指針往下一格，並且將新元素搬到慢指標的位置
                slow += 1
                nums[slow] = nums[fast]
                
        return slow + 1 
