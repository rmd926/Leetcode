# Cantor's diagonal argument
# 將input視為一個n*n矩陣，找對角線並且將對角線的數字全部翻轉

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            if nums[i][i] == "0":
                ans.append("1")
            else:
                ans.append("0")
        
        return "".join(ans)

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.36 MB Beats 23.18 %
