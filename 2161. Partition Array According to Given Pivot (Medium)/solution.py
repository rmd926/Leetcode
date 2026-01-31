class Solution:
    def pivotArray(self, nums: List[int], p: int) -> List[int]:
        left = []
        pivot = []
        right = []

        for num in nums:
            if num < p:
                left.append(num)
            elif num == p:
                pivot.append(num)
            else:
                right.append(num)
        
        return left + pivot + right

# Runtime: 17 ms Beats 93.96 %
# Memory: 34.15 MB Beats 26.91 %
