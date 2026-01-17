class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        res1, res2 = set(), set()

        for num in nums1:
            if num not in nums2:
                res1.add(num)
        
        for num in nums2:
            if num not in nums1:
                res2.add(num)
        
        return [list(res1), list(res2)]

# Runtime: 11 ms Beats 35.78 %
# Memory: 19.51 MB Beats 11.54 %
