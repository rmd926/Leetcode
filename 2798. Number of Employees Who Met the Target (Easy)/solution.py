class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for num in hours:
            if num >= target:
                count += 1
        return count

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.38 MB Beats 29.07 %
