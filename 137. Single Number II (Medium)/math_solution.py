# 數學解，直接先取set再把所有數字 * 3 再扣掉原始sum(nums) = ans * 2
# 因此再除以2即可得到答案

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return ((3*sum((set(nums))))-sum(nums))//2

# Runtime: 0 ms Beats 100.00 %
# Memory: 21.17 MB Beats 5.96 %
