'''
這題直接使用ord、chr把t多出來的char印出來
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        b = 0
        for char in s:
            a += (ord(char))
        for char in t:
            b += (ord(char))
        
        return chr(b - a)
