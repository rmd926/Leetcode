# 292. Nim Game (Easy)

## Question

You are playing the following Nim Game with your friend:

* Initially, there is a heap of stones on the table.
* You and your friend will alternate taking turns, and you go first.
* On each turn, the person whose turn it is will remove `1` to `3` stones from the heap.
* The one who removes the last stone is the winner.

Given `n`, the number of stones in the heap, return `true` if you can win the game assuming both you and your friend play optimally. Otherwise, return `false`.

> ### Example 1:
>
> * Input: `n = 4`
> * Output: `false`
> * Explanation:
>
>   * If you remove `1` stone, your friend removes `3` stones and wins.
>   * If you remove `2` stones, your friend removes `2` stones and wins.
>   * If you remove `3` stones, your friend removes the last stone and wins.
>
> In all outcomes, your friend wins.

> ### Example 2:
>
> * Input: `n = 1`
> * Output: `true`

> ### Example 3:
>
> * Input: `n = 2`
> * Output: `true`

## Constraints:

* `1 <= n <= 2^31 - 1`
