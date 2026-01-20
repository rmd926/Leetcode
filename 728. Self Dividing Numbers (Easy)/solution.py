from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for num in range(left, right+1):
            x = num
            status = True

            while x > 0:
                d = x % 10
                if d == 0 or num % d != 0: # 如果尾數是0，或者是說原本數字mod本身任一位數無法整除
                    status = False
                    break
                
                x //= 10
            
            if status:
                ans.append(num)

        return ans

# Runtime: 3 ms Beats 95.66 %
# Memory: 19.49 MB Beats 8.87 %
