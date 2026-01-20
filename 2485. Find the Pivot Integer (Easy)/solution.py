class Solution:
    def pivotInteger(self, n: int) -> int:
        record = [x for x in range(1, n+1)]
        
        for pivot in range(len(record)//2, len(record)+1):
            if sum(record[0: pivot+1]) == sum(record[pivot: ]):
                return pivot + 1
            else:
                continue
        
        return -1

# Runtime: 315 ms Beats 18.97 %
# Memory: 19.41 MB Beats 12.20 %
