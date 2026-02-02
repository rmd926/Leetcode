class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                count += i
        
        return count

# Runtime: 23 ms Beats 84.35 %
# Memory: 19.37 MB Beats 22.59 %
