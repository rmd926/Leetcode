# 3925. Concatenate Array With Reverse (Easy)

## Problem

You are given an integer array `nums` of length `n`.

Construct a new array `ans` of length `2 * n` such that:

* The first `n` elements are the same as `nums`
* The next `n` elements are the elements of `nums` in reverse order

Formally, for `0 <= i <= n - 1`:

```text
ans[i] = nums[i]
ans[i + n] = nums[n - i - 1]
```

Return the integer array `ans`.

## Examples

### Example 1

```text
Input: nums = [1,2,3]
Output: [1,2,3,3,2,1]
```

Explanation:

The first `n` elements of `ans` are the same as `nums`.

For the next `n = 3` elements, each element is taken from `nums` in reverse order:

```text
ans[3] = nums[2] = 3
ans[4] = nums[1] = 2
ans[5] = nums[0] = 1
```

Thus:

```text
ans = [1, 2, 3, 3, 2, 1]
```

### Example 2

```text
Input: nums = [1]
Output: [1,1]
```

Explanation:

The array remains the same when reversed.

Thus:

```text
ans = [1, 1]
```

## Constraints

```text
1 <= nums.length <= 100
1 <= nums[i] <= 100
```
