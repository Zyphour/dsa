# Insertion Sort

**Aim:** Sort 5 integers in ascending order using Insertion Sort.

**Language:** C++ · **Program:** [`insertion_sort.cpp`](insertion_sort.cpp)

---

## Concepts

- Works like sorting playing cards in your hand: take one element `key = a[i]`
  at a time and insert it into its proper spot inside the already-sorted prefix
  `a[0 .. i - 1]`.
- Elements larger than `key` are shifted right by one slot instead of being
  swapped repeatedly.

## Algorithm

1. Read 5 elements into `a[5]`.
2. For `i = 1` to `4`:
   - `key = a[i]`, `j = i - 1`.
   - While `j >= 0` and `a[j] > key`: set `a[j + 1] = a[j]`, `j--`.
   - Set `a[j + 1] = key`.
3. Print `a`.

## Complexity & Comparison

| Case | Input shape | Time |
|---|---|---|
| Best | Already sorted | **O(n)** (inner `while` never runs) |
| Average / Worst | Random / Reverse sorted | **O(n²)** |
| Space | In-place | **O(1)** |

## Exam points

- Fastest simple `O(n²)` sort on small or nearly-sorted arrays.
- Stable because shifting stops when `a[j] <= key`.
- `j >= 0` must be checked *before* `a[j] > key` to avoid reading `a[-1]`.
