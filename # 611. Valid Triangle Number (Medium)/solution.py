class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        
        for k in range(n-1, 1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j-i) #如果這個可以過，代表已知(j-i)筆會過，就不用額外再跑
                    j -= 1

                else:
                    i += 1
        return count

# Runtime: 455 ms Beats 45.97 %
# Memory: 19.58 MB Beats 14.99 %
