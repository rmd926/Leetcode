class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime) % 24

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.47 MB Beats 15.48 %
