class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            n = len(str(num))
            first_sum = 0
            last_sum = 0
            if n % 2 == 0:
                for i in range(0, n//2):
                    first_sum += int(str(num)[i])
                for i in range(n//2, n):
                    last_sum += int(str(num)[i])

                if first_sum == last_sum:
                    count += 1
                else:
                    continue
            else:
                continue
            
        return count

# Runtime: 548 ms Beats 57.17 %
# Memory: 19.46 MB Beats 10.13 %
