class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        
        return count
      
# Runtime: 0 ms Beats 100.00 %
# Memory: 19.42 MB Beats 10.64 %
