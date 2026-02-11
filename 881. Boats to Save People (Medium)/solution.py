class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        ans = 0
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            ans += 1
        
        return ans

# Runtime: 48 ms Beats 71.46 %
# Memory: 25.16 MB Beats 51.12 %
