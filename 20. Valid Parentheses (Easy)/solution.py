class Solution:
    def isValid(self, target) -> bool:
        stack = []
        map = {'}' : '{', ')' : '(' , ']' : '['}

        for char in target:
            if char in map.values():
                stack.append(char)
            
            elif char in map.keys():
                if not stack or map[char] != stack.pop():
                    return False
        
        return not stack # stack內所有元素都被pop掉時 = True，反之則是False

# Runtime: 3 ms Beats 36.88 %
# Memory: 19.31 MB Beats 14.26 %
