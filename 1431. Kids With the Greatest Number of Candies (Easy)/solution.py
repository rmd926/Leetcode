class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)
        status = False
        ans = []
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                status = True
                ans.append(status)
            else:
                status = False
                ans.append(status)
        return ans
