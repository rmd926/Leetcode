class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        temp = 0
        for i in range(1, len(points)):
            temp += max(abs(points[i-1][0] - points[i][0]), abs(points[i-1][1] - points[i][1]))
        
        return temp

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.29 MB Beatsd 91.56 %
