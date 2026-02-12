class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = Counter()
        for nums in nums1, nums2, nums3: freq.update(set(nums))
        return [k for k, v in freq.items() if v >= 2]

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.53 MB Beats 6.56 %
