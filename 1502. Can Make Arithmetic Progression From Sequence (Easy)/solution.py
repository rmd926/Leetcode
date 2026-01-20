class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.42 MB Beats 8.30 %
