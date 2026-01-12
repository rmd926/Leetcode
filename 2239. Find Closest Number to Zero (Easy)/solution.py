class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_distance = -100000000
        for i in nums:
            if abs(i) < abs(min_distance):
                min_distance = i
                
        if min_distance < 0 and abs(min_distance) in nums:
            return abs(min_distance)
        else:
            return min_distance
