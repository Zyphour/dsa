# Student Guide — `heap_sort.py`

This guide explains how [`heap_sort.py`](heap_sort.py) works and prepares you for viva questions.

## How the Code Works

- **`heapify(a, n, i)`:** Notice `n` is passed as an argument instead of using `len(a)`. Why? During the extraction loop, the sorted elements accumulate at the end of `a`, so we need `heapify` to treat only the **first `i` elements** as the active heap!
  - `left = 2 * i + 1` and `right = 2 * i + 2` are the 0-based child formulas.
  - Compares `a[i]`, `a[left]`, and `a[right]` to find `largest`. If a child is bigger, it swaps and keeps pushing the smaller value downward.
- **`heap_sort(a)`:**
  - `range(n // 2 - 1, -1, -1)` starts at the last node that actually has children (`n // 2 - 1`), because leaf nodes (`n // 2` to `n - 1`) have no children and are already valid heaps.
  - The second loop swaps `a[0]` with `a[i]` (locking the max element into `a[i]`) and calls `heapify(a, i, 0)` on the smaller heap of size `i`.

## Dry Run — `[4, 10, 3, 5, 1]`

1. **Build Max-Heap** (`n = 5`, `n // 2 - 1 = 1`):
   - `heapify(..., 1)`: `10` > `5, 1` (no change)
   - `heapify(..., 0)`: `10` > `4, 3` → swap `4, 10` → `[10, 4, 3, 5, 1]` → recurse at `1` → swap `4, 5` → `[10, 5, 3, 4, 1]`.
2. **Extract & Sort:**
   - `i = 4`: swap `10, 1` → `[1, 5, 3, 4 | 10]` → `heapify(4, 0)` → `[5, 4, 3, 1 | 10]`
   - `i = 3`: swap `5, 1` → `[1, 4, 3 | 5, 10]` → `heapify(3, 0)` → `[4, 1, 3 | 5, 10]`
   - `i = 2`: swap `4, 3` → `[3, 1 | 4, 5, 10]` → `heapify(2, 0)` → `[3, 1 | 4, 5, 10]`
   - `i = 1`: swap `3, 1` → `[1, 3, 4, 5, 10]`

Output: `[1, 3, 4, 5, 10]`

## Common Mistakes

- Passing `len(a)` instead of `i` into `heapify(a, i, 0)` during extraction — that accidentally pulls already-sorted numbers back into the heap!
- Using 1-based formulas (`2*i` and `2*i + 1`) on a 0-based Python list.

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Why do we build a **Max-Heap** to sort in **ascending** order? | Because the largest value at `a[0]` gets swapped straight to the end (`a[n-1]`), leaving the smallest items at the front. |
| Why does building the heap start at `n // 2 - 1`? | Indices from `n // 2` to `n - 1` are leaf nodes with no children, so they already satisfy the heap property. |
| Is Heap Sort stable? | No, swapping `a[0]` to the end can change the relative order of equal keys. |
| What is the worst-case time complexity? | `O(n log n)`. |
