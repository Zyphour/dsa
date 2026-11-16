# Selection Sort

**Aim:** Sort an array of integers in ascending order using Selection Sort.

**Language:** C++ · **Program:** [`selection_sort.cpp`](selection_sort.cpp)

---

## Concepts

- Divide the array into a **sorted prefix** (left) and an **unsorted suffix**
  (right).
- On pass `i`, scan the unsorted suffix `i .. n - 1` to find the **index of the
  minimum element**, then swap it into `arr[i]`.

## Algorithm

1. Read `n` and `n` elements into `arr`.
2. For `i = 0` to `n - 2`:
   - Set `min = i`.
   - For `j = i + 1` to `n - 1`: if `arr[j] < arr[min]`, set `min = j`.
   - Swap `arr[i]` and `arr[min]`.
3. Print `arr`.

## Comparison

| | Selection Sort | Bubble Sort |
|---|---|---|
| Idea | pick min, 1 swap per pass | swap adjacent out-of-order pairs |
| Comparisons | O(n²) always | O(n²) |
| Swaps | at most `n - 1` (O(n)) | up to `n(n - 1)/2` (O(n²)) |
| Space | O(1) | O(1) |

## Exam points

- Always does `O(n²)` comparisons even if the array is already sorted.
- Useful when memory writes/swaps are expensive because it makes at most `n - 1`
  swaps.
- Not stable in standard form because a long-distance swap can jump over equal
  elements.
