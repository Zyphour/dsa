# Practical 7 — Merge Sort

**Aim:** Sort a list in ascending order using recursive Divide-and-Conquer Merge
Sort.

**Language:** Python · **Program:** [`merge_sort_orders.py`](merge_sort_orders.py)

---

## Concepts

- **Divide and Conquer:**
  1. **Divide** the array at `mid = len(a) // 2` into `left` and `right`.
  2. **Conquer** by sorting each half recursively (base case: `len(a) <= 1`).
  3. **Merge** two sorted halves in linear time by comparing their front items.
- **Stable sort** – picking `left[i]` when `left[i] <= right[j]` preserves the
  original order of equal elements.

## Algorithm

1. If `len(a) <= 1`, return `a`.
2. Split `left = merge_sort(a[:mid])`, `right = merge_sort(a[mid:])`.
3. Initialize `result = []`, `i = 0`, `j = 0`.
4. While `i < len(left)` and `j < len(right)`:
   - Append smaller of `left[i]` and `right[j]` to `result` and advance its
     index.
5. Append remaining items `left[i:]` and `right[j:]` to `result` and return it.

## Comparison

| | Merge Sort | Heap Sort |
|---|---|---|
| Time (all cases) | O(n log n) | O(n log n) |
| Extra space | O(n) | O(1) |
| Stable? | Yes | No |

## Exam points

- Every level splits in half (`log₂ n` levels) and merges `n` elements →
  guaranteed **O(n log n)** even in the worst case.
- Needs **O(n)** auxiliary space (not in-place for arrays).
- Ideal for linked lists and external sorting (large files on disk).
