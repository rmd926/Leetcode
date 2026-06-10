class Solution:
    def isHappy(self, n: int) -> bool:
        status = True
        temp = []

        while n not in temp and n != 1:
            temp.append(n)
            target = str(n)
            cur = 0

            for ch in target:
                cur += int(ch) ** 2
            
            n = cur
        
        if n == 1:
            status = True
        else:
            status = False

        return status

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.33 MB Beats 23.20 %
