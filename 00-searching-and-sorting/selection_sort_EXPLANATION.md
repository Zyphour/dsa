# Student Guide — `selection_sort.cpp`

This guide explains how [`selection_sort.cpp`](selection_sort.cpp) works and prepares you for viva questions.

## How the Code Works

```cpp
for(int i = 0; i < n - 1; i++) {
    int min = i;
    for(int j = i + 1; j < n; j++)
        if(arr[j] < arr[min]) min = j;
    temp = arr[i]; arr[i] = arr[min]; arr[min] = temp;
}
```
- **Outer loop (`i`):** Picks the next position `i` (`0` to `n - 2`) where the next smallest number belongs.
- **`int min = i;`:** Assumes `arr[i]` is the smallest element in the unsorted part `i .. n - 1` (remember: `min` stores the **index**, not the value!).
- **Inner loop (`j`):** Checks every element after `i`. Whenever it sees a smaller value (`arr[j] < arr[min]`), it updates `min = j`.
- **Swap after the inner loop:** Once the inner loop finishes scanning, `min` holds the index of the smallest element, so we swap `arr[i]` and `arr[min]` just once.

## Dry Run

Input: `n = 4`, `arr = [64, 25, 12, 22]`

| Pass `i` | Unsorted part | Minimum found | Array after swap |
|---|---|---|---|
| `0` | `[64, 25, 12, 22]` | `12` (index `2`) | `[12, 25, 64, 22]` |
| `1` | `[25, 64, 22]` | `22` (index `3`) | `[12, 22, 64, 25]` |
| `2` | `[64, 25]` | `25` (index `3`) | `[12, 22, 25, 64]` |

Output: `Sorted array: 12 22 25 64`

## Common Mistakes

- Storing the *value* in `min` (`min = arr[i]`) instead of its *index* (`min = i`), which breaks the swap at the end!
- Putting the swap *inside* the inner `j` loop instead of *after* it (that turns it into messy extra swaps instead of Selection Sort).
- Starting `j` at `0` instead of `i + 1` (ruins the already-sorted left side).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| How is Selection Sort different from Bubble Sort? | Selection Sort finds the minimum first and does only 1 swap per pass (`O(n)` swaps total), while Bubble Sort can swap on every comparison (`O(n²)` swaps). |
| What is the best-case time complexity of Selection Sort? | Still `O(n²)`, because it always checks the entire remaining unsorted part to be sure it found the minimum. |
| Why does `i` only go up to `n - 2`? | After placing the first `n - 1` smallest elements, the last element is automatically the biggest. |
