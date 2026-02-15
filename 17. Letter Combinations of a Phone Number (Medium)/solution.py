import itertools
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        groups = []
        for d in digits:
            groups.append(mapping[d])  # 每一位數字對應的字母集合（字串）

        ans = []
        for ch in itertools.product(*groups):   # 每一組各取一個字母
            ans.append("".join(ch))

        return ans
