class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        
        for key, value in lookup.items():
            if value % 2 != 0:
                return False
        return True

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.35 MB Beats 47.84 %
