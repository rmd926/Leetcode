class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 就這^^
        return sum(nums) % k
