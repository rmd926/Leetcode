class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original_sum = sum(nums)
        unique_sum = sum(set(nums))
        n = len(nums)

        return [(original_sum - unique_sum), n * (n + 1) // 2 - unique_sum]

# Runtime: 1 ms Beats 97.73 %
# Memory: 21.32 MB Beats 5.03 %
