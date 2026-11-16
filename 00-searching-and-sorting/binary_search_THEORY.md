# Binary Search

**Aim:** Find a target value in a **sorted** array by repeatedly halving the
search interval.

**Language:** C++ · **Program:** [`binary_search.cpp`](binary_search.cpp)

---

## Concepts

- **Divide and conquer** – inspect the middle element `arr[mid]`; one
  comparison eliminates half of the remaining array.
- **Prerequisite** – the array **must already be sorted**; otherwise the halving
  logic breaks.

## Algorithm

1. Set `low = 0`, `high = n - 1`.
2. While `low <= high`:
   - `mid = (low + high) / 2`
   - If `arr[mid] == key` → print `mid + 1` and exit.
   - If `arr[mid] < key` → search right half (`low = mid + 1`).
   - Else → search left half (`high = mid - 1`).
3. If `low > high`, print `"Element not found."`

## Comparison

| | Linear Search | Binary Search |
|---|---|---|
| Input order | any | sorted only |
| Best / Worst time | O(1) / O(n) | O(1) / O(log n) |
| Steps for 1,000 items (worst) | 1,000 | ~10 |

## Exam points

- Loop condition must be `low <= high` (not `<`), otherwise a 1-element range is
  skipped.
- Update bounds to `mid + 1` or `mid - 1` (never `mid`) so the loop always
  shrinks and terminates.
- Binary search is O(log n) because the range halves on every step.
