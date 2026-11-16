# Student Guide — `insertion_sort.cpp`

This guide explains how [`insertion_sort.cpp`](insertion_sort.cpp) works and prepares you for viva questions.

## How the Code Works

```cpp
for (int i = 1; i < 5; i++) {
    key = a[i]; j = i - 1;
    while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
    a[j + 1] = key;
}
```
- **Why `i = 1`?** Index `0` (`a[0]`) is a 1-element list, so it's already sorted! We start picking elements from index `1`.
- **`key = a[i];`** Saves the current element before shifting numbers over `a[i]`.
- **`j = i - 1;`** Starts comparing with the element right to the left of `key`.
- **`while (j >= 0 && a[j] > key)`:**
  - `j >= 0` stops us from reading before index `0`.
  - `a[j] > key` checks if the sorted element on the left is bigger than `key`. If yes, it shifts `a[j]` one spot right (`a[j + 1] = a[j]`) and moves `j` left (`j--`).
- **`a[j + 1] = key;`** Once the `while` loop stops (either `j` hit `-1` or `a[j] <= key`), the open slot is `j + 1`, so `key` goes right there.

## Dry Run

Input: `a = [9, 5, 1, 4, 3]`

| `i` | `key` | Shifts in `while` | Array after inserting `key` |
|---|---|---|---|
| `1` | `5` | `9` shifts right | `[5, 9, 1, 4, 3]` |
| `2` | `1` | `9`, `5` shift right | `[1, 5, 9, 4, 3]` |
| `3` | `4` | `9`, `5` shift right | `[1, 4, 5, 9, 3]` |
| `4` | `3` | `9`, `5`, `4` shift right | `[1, 3, 4, 5, 9]` |

Output: `Sorted array: 1 3 4 5 9`

## Common Mistakes

- Forgetting `j >= 0` in the `while` condition (or checking `a[j] > key && j >= 0` in the wrong order, which reads `a[-1]` out of bounds!).
- Putting `a[j] = key` instead of `a[j + 1] = key` at the end (remember `j` was decremented one extra time before the loop stopped!).
- Starting the `for` loop at `i = 0` instead of `i = 1`.

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| When is Insertion Sort `O(n)`? | When the array is already sorted, because `a[j] > key` is immediately false on every step. |
| Why do we check `j >= 0` before `a[j] > key`? | Short-circuit evaluation: if `j` is `-1`, C++ stops immediately and never touches `a[-1]`. |
| Does Insertion Sort swap or shift? | It shifts larger elements right instead of doing 3-line swaps, which makes it faster in practice than Bubble Sort. |
| Is Insertion Sort stable? | Yes, because it only shifts when `a[j] > key` (strictly greater), keeping equal values in order. |
