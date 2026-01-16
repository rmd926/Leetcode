class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        
        for key, value in lookup.items():
            if value == 1:
                return key

# Runtime 3 ms Beats 72.61%
# Memory 20.91 MB Beats 5.96%
