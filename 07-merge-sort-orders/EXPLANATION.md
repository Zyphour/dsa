# Student Guide — `merge_sort_orders.py`

This guide explains how [`merge_sort_orders.py`](merge_sort_orders.py) works and prepares you for viva questions.

## How the Code Works

- **Stopping condition (`if len(a) <= 1: return a`):** Without this, recursion would keep slicing empty lists forever. Any 1-element list is already sorted.
- **Splitting (`a[:mid]` and `a[mid:]`):** Divides `a` into two halves and solves each recursively before merging.
- **Merging (`while i < len(left) and j < len(right)`):**
  - Imagine two already-sorted stacks of cards (`left` and `right`). You only ever need to compare their top cards (`left[i]` vs `right[j]`) to know which card is smaller overall!
  - Using `<=` (`left[i] <= right[j]`) picks from `left` first on ties — that is what makes Merge Sort **stable**.
- **Leftovers (`result += left[i:]`, `result += right[j:]`):** The `while` loop stops as soon as *one* half finishes, so one of the two halves still has 1 or more larger elements left. Only one of `left[i:]` or `right[j:]` is non-empty, and appending both safely copies the rest.

## Dry Run — `[8, 3, 5, 1, 9, 2]`

- Split: `[8, 3, 5]` and `[1, 9, 2]`
- Left splits down to `[8]`, `[3]`, `[5]` → merges `[3, 5]` → merges with `[8]` → **`[3, 5, 8]`**
- Right splits down to `[1]`, `[9]`, `[2]` → merges `[2, 9]` → merges with `[1]` → **`[1, 2, 9]`**
- Final merge of `[3, 5, 8]` and `[1, 2, 9]`:
  - `1` (`right`) → `2` (`right`) → `3` (`left`) → `5` (`left`) → `8` (`left`) → leftover `9` (`right`)
  - Result: **`[1, 2, 3, 5, 8, 9]`**

## Common Mistakes

- Forgetting to append the leftover elements (`left[i:]` and `right[j:]`) after the `while` loop ends — drops the largest elements!
- Missing the `len(a) <= 1` base case (causes `RecursionError`).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| What algorithmic technique does Merge Sort use? | Divide and Conquer. |
| Why is Merge Sort `O(n log n)` even in the worst case? | It always splits the array strictly in half (`log n` levels) and merges `n` elements per level regardless of input order. |
| Is Merge Sort stable and in-place? | It is **stable**, but **not in-place** (needs `O(n)` extra space). |
| When would you choose Merge Sort over Quick Sort? | When stability is required, for linked lists, or when worst-case `O(n log n)` is guaranteed. |
