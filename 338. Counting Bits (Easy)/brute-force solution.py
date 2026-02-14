# Brute-Force using bin tools
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for num in range(0, n+1):
            temp = (bin(num)[2:])
            count = 0
            for char in temp:
                if char == "1":
                    count += 1
                    
            ans.append(count)

        return ans

# Runtime: 38 ms Beats 20.90 %
# Memory: 20.32 MB Beats 29.66 %
