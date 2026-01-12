````md
# 1768. Merge Strings Alternately (Easy)

## 題目說明
給定兩個字串 `word1`、`word2`，請從 `word1` 開始交錯（alternating）地依序取字元合併成新字串：  
`word1[0] + word2[0] + word1[1] + word2[1] + ...`  
若其中一個字串較長，將剩下的字元直接接到結果尾端。回傳合併後的字串。

## Examples

### Example 1
Input: `word1 = "abc"`, `word2 = "pqr"`  
Output: `"apbqcr"`  
Explanation:
```text
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
````

### Example 2

Input: `word1 = "ab"`, `word2 = "pqrs"`
Output: `"apbqrs"`
Explanation:

```text
word1:  a   b
word2:    p   q   r   s
merged: a p b q r s
```

### Example 3

Input: `word1 = "abcd"`, `word2 = "pq"`
Output: `"apbqcd"`
Explanation:

```text
word1:  a   b   c   d
word2:    p   q
merged: a p b q c d
```

## Constraints

* `1 <= word1.length, word2.length <= 100`
* `word1` 與 `word2` 皆由小寫英文字母組成
