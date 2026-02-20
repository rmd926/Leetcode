class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1

            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                return [left+1, right+1]

# Runtime: 3 ms Beats 80.36 %
# Memory: 20.57 MB Beats 57.94 %
