
---

# 299. Bulls and Cows (Medium)

### Question

You are playing the **Bulls and Cows** game. You are given a `secret` number and a `guess`. Provide a hint in the format `"xAyB"`:

* **Bulls (A)**: Digits in the guess that are in the correct position.
* **Cows (B)**: Digits in the guess that exist in the secret number but are in the wrong position.

**Note:** If there are duplicate digits, each digit in the `guess` can only be matched with a unique digit in the `secret`.

**Example 1:**

* **Input:** `secret = "1807"`, `guess = "7810"`
* **Output:** `"1A3B"`

**Example 2:**

* **Input:** `secret = "1123"`, `guess = "0111"`
* **Output:** `"1A1B"`

---



這份筆記把 **Example 2** 的重複數字處理邏輯說得很清楚了。如果之後你想挑戰進階寫法（例如只用一次迴圈），我們也可以再討論！需要我幫你整理下一題嗎？
