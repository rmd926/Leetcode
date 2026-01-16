class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s, ptr_t = 0, 0

        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
    
            ptr_t += 1
        return ptr_s == len(s) # 如果ptr_s已經搜完則True；反之則False
