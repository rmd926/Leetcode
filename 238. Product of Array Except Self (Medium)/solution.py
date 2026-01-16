# O(n^2) TLE QQ
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             temp = nums[0:i] + nums[i+1:]
#             value = 1
#             for j in range(len(temp)):
#                 value *= temp[j]
#             ans.append(value)
#         return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # res[i] = product of nums[0..i-1]
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # multiply by product of nums[i+1..n-1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
