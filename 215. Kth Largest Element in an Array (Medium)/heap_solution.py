import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
      
# Runtime: 87 ms Beats 57.22 %
# Memory: 31.10 MB Beats 35.78 %
