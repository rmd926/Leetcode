class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0

        while left < right: # 確保左指針不會超車右指針
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            
            elif height[left] < height[right]:
                left += 1

            else:
                right -= 1
                
        return area
