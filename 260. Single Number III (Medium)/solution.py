class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        
        ans = []
        for key, value in lookup.items():
            if value == 1:
                ans.append(key)
    
        return ans

# Runtime: 3 ms Beats 63.82%
# Memory: 21.23 MB Beats 8.16%
