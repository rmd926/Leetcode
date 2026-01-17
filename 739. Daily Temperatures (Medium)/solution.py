from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []  # 存 index，且保持 temperatures[stack] 單調遞減

        for i, cur_temp in enumerate(temperatures):
            # 只要今天比較熱，就把前面較冷(或不夠熱)的日子結算掉
            while stack and cur_temp > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev  # 等到更熱那天要等幾天

            stack.append(i)

        return ans

# Runtime: 94 ms Beats 62.32 %
# Memory: 28.66 MB Beats 38.42 %
