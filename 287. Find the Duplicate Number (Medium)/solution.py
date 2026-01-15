'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = list(set(nums))
        ans = (sum(nums) - sum(temp)) // (len(nums) - len(temp)) 
        return ans
