class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # 拆分日期字串
        year, month, day = map(int, date.split("-"))
        
        year_bin = bin(year)[2:]
        month_bin = bin(month)[2:]
        day_bin = bin(day)[2:]
        
        # 用 '-' 連接
        return year_bin+"-"+month_bin+"-"+day_bin
