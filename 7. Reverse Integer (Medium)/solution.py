class Solution(object):
    def reverse(self, x):
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31

        if x > 0 :
            ans = int(str(x)[::-1])
        elif x < 0:
            ans = -int(str(abs(x))[::-1])
        else:
            return 0
        
        if ans > max_int or ans < min_int: #dealing with the overflow problem
            return 0
        else:
            return ans
