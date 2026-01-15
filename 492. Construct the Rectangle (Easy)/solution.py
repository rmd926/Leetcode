'''
想法: 從平方根開始出發，因為要讓[L, W]符合L >= W，且兩者越近越好。
接下來就是去求比較小的W，所以逐次W -= 1，去看有沒有辦法整除，如果不行則繼續-= 1直到可以被整除時:
return [area//temp, temp]
'''
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        temp = int(area ** 0.5)
        while area % temp != 0:
            temp -= 1
        return [area//temp, temp]
