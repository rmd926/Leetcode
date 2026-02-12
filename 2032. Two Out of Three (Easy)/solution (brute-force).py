class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        lookup = {}
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        for num in set1:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1

        for num in set2:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
                
        for num in set3:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1

        ans = []
        for key, value in lookup.items():
            if value >= 2:
                ans.append(key)

        return ans

# Runtime: 5 ms Beats 27.10 %
# Memory:　19.47 MB Beats 26.96 %
