class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        ans = temp
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                ans = max(temp, ans)
            else:
                temp = 0
        return ans

# Runtime: 19 ms Beats 55.21 %
# Memory: 21.88 MB Beats 16.93 %
