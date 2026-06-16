# 3005. Count Elements With Maximum Frequency (Easy)

## Problem

You are given an array `nums` consisting of positive integers.

Return the total frequencies of elements in `nums` such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

## Examples

### Example 1

```text
Input: nums = [1,2,2,3,1,4]
Output: 4
```

Explanation:

The elements `1` and `2` both have a frequency of `2`, which is the maximum frequency in the array.

```text
1 -> 2 times
2 -> 2 times
3 -> 1 time
4 -> 1 time
```

So the total frequency of elements with maximum frequency is:

```text
2 + 2 = 4
```

### Example 2

```text
Input: nums = [1,2,3,4,5]
Output: 5
```

Explanation:

Every element appears once, so the maximum frequency is `1`.

There are `5` elements with this maximum frequency, so the answer is `5`.

## Constraints

```text
1 <= nums.length <= 100
1 <= nums[i] <= 100
```

## Approach

Use a dictionary to count the frequency of each number.

Then find the maximum frequency.

Finally, add up all frequencies that are equal to the maximum frequency.

## Code

```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        lookup = {}

        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1

        max_freq = max(lookup.values())

        ans = 0

        for freq in lookup.values():
            if freq == max_freq:
                ans += freq

        return ans
```

## Complexity Analysis

Let `n` be the length of `nums`.

### Time Complexity

```text
O(n)
```

We iterate through the array once to count frequencies, and then iterate through the frequency table.

### Space Complexity

```text
O(n)
```

In the worst case, every number is different, so the dictionary stores up to `n` elements.
