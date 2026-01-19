class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)

        for num in nums:
            seen.add(num)
        
        ans = []
        for i in range(1, n+1):
            if i not in seen:
                ans.append(i)
                
        return ans

# Runtime: 34 ms Beats 43.23 %
# Memory: 31.08 MB Beats 48.64 %
