class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
            
        ans = 0
        for key, value in lookup.items():
            if value == 1:
                ans += key

        return ans

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.38 MB Beats 31.87 %
