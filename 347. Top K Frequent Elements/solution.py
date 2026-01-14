'''
Time Complexity: O(nlogn)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        ans = []
        for key, value in sorted(lookup.items(), key = lambda x: (-x[1], x[0])):
            ans.append(key)
            if len(ans) == k:
                return ans
