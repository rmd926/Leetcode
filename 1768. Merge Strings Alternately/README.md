```md
# 1768. Merge Strings Alternately

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

Example 1  
Input: `word1 = "abc", word2 = "pqr"`  
Output: `"apbqcr"`  
Explanation:
```

word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

```

Example 2  
Input: `word1 = "ab", word2 = "pqrs"`  
Output: `"apbqrs"`  
Explanation: `word2` is longer, so `"rs"` is appended to the end.
```

word1:  a   b
word2:    p   q   r   s
merged: a p b q r s

```

Example 3  
Input: `word1 = "abcd", word2 = "pq"`  
Output: `"apbqcd"`  
Explanation: `word1` is longer, so `"cd"` is appended to the end.
```

word1:  a   b   c   d
word2:    p   q
merged: a p b q c d

````

Constraints  
- `1 <= word1.length, word2.length <= 100`  
- `word1` and `word2` consist of lowercase English letters.

Approach  
Use two pointers and build the result with a list: alternately append characters while both strings have remaining characters, then append the remaining substring of the longer string. Time complexity is `O(n+m)` and space complexity is `O(n+m)` for the output.

Python Solution  
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        n1, n2 = len(word1), len(word2)
        while i < n1 and i < n2:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        res.append(word1[i:])
        res.append(word2[i:])
        return "".join(res)
````

```
::contentReference[oaicite:0]{index=0}
```
