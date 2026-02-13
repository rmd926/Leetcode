class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp = []
        while len(nums) > 1:
            for i in range(1, len(nums)):
                temp.append((nums[i-1] + nums[i]) % 10)
            nums = temp
            temp = []

        return nums[0]

# Runtime: 1155 ms Beats 55.69 %
# Memory: 19.44 MB Beats 37.90 %
