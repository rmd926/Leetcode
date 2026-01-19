class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(0, len(nums)//2):
            for j in range(i, len(nums), n):
                ans.append(nums[j])

        return ans
        
# Runtime: 60 ms Beats 45.78 %
# Memory: 19.38 MB Beats 17.85 %
