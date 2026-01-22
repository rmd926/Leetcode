class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums = sorted(nums)
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            prev = nums[i-1]
            while diff > 1:
                prev += 1
                ans.append(prev)
                diff -= 1
            
        return ans

# Runtime: 3 ms Beats 71.69 %
# Memory: 19.50 MB Beats 5.59 %

# Brute-Force Methods:
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        gt = [i for i in range(min(nums), max(nums)+1)]
        for num in nums:
            if num in gt:
                gt.remove(num)
        
        return gt

# Runtime: 10 ms Beats 5.91 %
# Memory: 19.40 MB Beats 5.59 %
