# Student Guide — `bubble_sort.cpp`

This guide explains how [`bubble_sort.cpp`](bubble_sort.cpp) sorts an array and covers likely exam questions.

## How the Code Works

```cpp
for (int i = 0; i < n - 1; i++)
    for (int j = 0; j < n - i - 1; j++)
        if (a[j] > a[j + 1]) { temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp; }
```
- **Outer loop (`i`):** Runs `n - 1` passes. Why `n - 1`? Once `n - 1` elements are in their right places, the 1 element left over is automatically in place!
- **Inner loop (`j`):** Walks from `0` up to `n - i - 2` (since `< n - i - 1`), comparing `a[j]` with its right neighbor `a[j + 1]`.
- **Why `- i`?** After `i` passes, the last `i` elements at the end of the array are already the `i` largest elements in their final spots, so checking them again would be wasted work.
- **Swapping:** Uses a third variable `temp` so we don't overwrite `a[j]` before saving its value.

## Dry Run

Input: `n = 4`, `a = [5, 1, 4, 2]`

- **Pass `i = 0`** (`j` goes `0..2`):
  - `5 > 1` → swap → `[1, 5, 4, 2]`
  - `5 > 4` → swap → `[1, 4, 5, 2]`
  - `5 > 2` → swap → `[1, 4, 2, 5]` (`5` is locked at the end!)
- **Pass `i = 1`** (`j` goes `0..1`):
  - `1 > 4`? No.
  - `4 > 2` → swap → `[1, 2, 4, 5]` (`4` is locked!)
- **Pass `i = 2`** (`j` goes `0..0`):
  - `1 > 2`? No.

Output: `Sorted array: 1 2 4 5`

## Common Mistakes

- Letting `j` go up to `n - 1` instead of `n - i - 1` — `a[j + 1]` then reads `a[n]`, which is out of bounds!
- Using `a[j] < a[j + 1]` by mistake (that sorts in *descending* order instead of ascending).
- Overwriting `a[j] = a[j + 1]` before copying `temp = a[j]`.

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Why does Bubble Sort have `O(n²)` time complexity? | Because for `n` items it uses two nested loops doing roughly `n*(n-1)/2` comparisons. |
| Can Bubble Sort be improved to `O(n)` on an already-sorted array? | Yes — keep a `swapped` flag in each pass and `break` early if no swaps happened. |
| Is Bubble Sort stable? | Yes, because it only swaps when `a[j] > a[j + 1]`, keeping equal elements in order. |
| How many passes does it take for `n` elements? | At most `n - 1` passes. |
