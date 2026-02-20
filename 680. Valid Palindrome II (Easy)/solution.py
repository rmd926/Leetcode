class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return helper(left+1, right) or helper(left, right-1)
            left += 1
            right -= 1
        return True

# Runtime: 55 ms Beats 70.04 %
# Memory: 19.62 MB Beats 36.55 %
