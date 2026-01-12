```md
# 1768. Merge Strings Alternately

## 題目描述
給定兩個字串 `word1` 與 `word2`，請從 `word1` 開始，依序交替取字元合併成新字串。  
若其中一個字串較長，則將剩餘的字元直接接到合併結果的尾端。

請回傳合併後的字串。

---

## 範例

### Example 1
**Input:** `word1 = "abc"`, `word2 = "pqr"`  
**Output:** `"apbqcr"`  
**Explanation:**
```

word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

```

### Example 2
**Input:** `word1 = "ab"`, `word2 = "pqrs"`  
**Output:** `"apbqrs"`  
**Explanation:** `word2` 較長，因此將剩下的 `"rs"` 接在最後
```

word1:  a   b
word2:    p   q   r   s
merged: a p b q r s

```

### Example 3
**Input:** `word1 = "abcd"`, `word2 = "pq"`  
**Output:** `"apbqcd"`  
**Explanation:** `word1` 較長，因此將剩下的 `"cd"` 接在最後
```

word1:  a   b   c   d
word2:    p   q
merged: a p b q c d

```

---

## 限制條件
- `1 <= word1.length, word2.length <= 100`
- `word1` 和 `word2` 皆由小寫英文字母組成
```
