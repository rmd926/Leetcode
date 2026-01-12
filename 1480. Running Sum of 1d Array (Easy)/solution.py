class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        ans = []
        for i in range(len(nums)):
            temp += nums[i]
            ans.append(temp)
        return ans
