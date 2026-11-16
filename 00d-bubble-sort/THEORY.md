# Bubble Sort

**Aim:** Sort an array of integers in ascending order using Bubble Sort.

**Language:** C++ · **Program:** [`bubble_sort.cpp`](bubble_sort.cpp)

---

## Concepts

- **Adjacent comparison & swap** – step through the array comparing `a[j]` and
  `a[j + 1]`; swap if `a[j] > a[j + 1]`.
- After pass `i`, the `i + 1` largest elements have "bubbled" to their final
  spots at the end of the array.

## Algorithm

1. Read `n` and `n` elements into `a`.
2. For `i = 0` to `n - 2`:
   - For `j = 0` to `n - i - 2`:
     - If `a[j] > a[j + 1]`, swap `a[j]` and `a[j + 1]`.
3. Print the sorted array.

## Comparison

| Sort | Time (Best / Worst) | Swaps | Stable? |
|---|---|---|---|
| Bubble Sort | O(n²) / O(n²) *(O(n) with early-exit flag)* | O(n²) | Yes |
| Selection Sort | O(n²) / O(n²) | O(n) | No |
| Insertion Sort | O(n) / O(n²) | shifts, O(n²) | Yes |

## Exam points

- Inner loop stops at `n - i - 1` because the last `i` elements are already
  sorted.
- Sorts in place (`O(1)` extra space).
- Stable because equal elements (`a[j] == a[j + 1]`) are never swapped.
