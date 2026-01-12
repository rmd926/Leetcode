1768. Merge Strings Alternately
難度： Easy | 標籤： Two Pointers String

題目描述
給你兩個字串 word1 和 word2。請將這兩個字串以交替順序合併，並從 word1 開始。如果其中一個字串比另一個長，請將剩餘的字母附加在合併後字串的末尾。

最後回傳合併後的字串。

範例說明
Example 1:
Input: word1 = "abc", word2 = "pqr"

Output: "apbqcr"

Explanation: 合併過程如下：

Plaintext

word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:
Input: word1 = "ab", word2 = "pqrs"

Output: "apbqrs"

Explanation: 由於 word2 較長，"rs" 會被附加在結尾。

Plaintext

word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:
Input: word1 = "abcd", word2 = "pq"

Output: "apbqcd"

Explanation: 由於 word1 較長，"cd" 會被附加在結尾。

Plaintext

word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
限制條件
1 <= word1.length, word2.length <= 100

word1 和 word2 由小寫英文字母組成。
