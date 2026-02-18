class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies_list = [1] * n
        # 做兩次遍歷，先從左到右搜一次
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies_list[i] = candies_list[i-1] + 1
        # 由右搜到左時，檢查左邊是否有比右邊分數大的，若有則對 ［當前糖果個數］以及［其右邊之糖果個數+1］取max
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies_list[i-1] = max(candies_list[i-1], candies_list[i]+1)
        
        return sum(candies_list)

# Runtime: 15 ms Beats 71.82 %
# Memory: 21.57 MB Beats 34.97 %
