class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k]) # 初始設定前k個取sum()
        window_sum = temp

        for i in range(k, len(nums)): # 從窗口的下一個開始for loop
            window_sum += (nums[i] - nums[i-k]) # 加滑窗右邊一個元素，減去原本最左邊
            temp = max(temp, window_sum)

        return temp / k

# Runtime: 51 ms Beats 88.87%
# Memory: 29.22 MB Beats 9.48%
