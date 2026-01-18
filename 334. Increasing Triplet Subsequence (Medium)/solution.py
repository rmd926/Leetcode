class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # i < j < k
        i = float("inf")
        j = float("inf")
        
        for num in nums:
            if num <= i: # 先更新i再更新j，最後有比j大的就符合 i < j < k
                i = num

            elif num <= j:
                j = num
            
            elif num > j:
                return True
            
        return False # 掃描完畢仍未找到triplet

# Runtime: 13 ms Beats 78.27 %
# Memory: 39.03 MB Beats 7.50 %
