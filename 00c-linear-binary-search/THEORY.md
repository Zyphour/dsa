# Linear & Binary Search (Menu)

**Aim:** Provide a menu-driven C++ program to search an array using either
Linear Search or Binary Search.

**Language:** C++ · **Program:** [`linear_binary_search.cpp`](linear_binary_search.cpp)

---

## Concepts

- **Linear Search** checks elements one by one from index `0` to `n - 1` (works
  on any array).
- **Binary Search** splits a **sorted** array in half repeatedly using `low`,
  `high`, and `mid`.

## Algorithm

1. Read `n`, read `n` elements into `arr`, read menu `choice` (`1` or `2`), and
   read `key`.
2. Switch on `choice`:
   - **Case 1 (Linear):** scan `0 .. n - 1`; print `i + 1` on match, else `"Element not found."`
   - **Case 2 (Binary):** maintain `low = 0, high = n - 1`; loop `low <= high`,
     check `arr[mid]`, and shrink left or right half.
   - **Default:** print `"Invalid Choice!"`.

## Comparison

| Method | Prerequisite | Time | Space |
|---|---|---|---|
| Linear Search | None | O(n) | O(1) |
| Binary Search | Sorted array | O(log n) | O(1) |

## Exam points

- Only pick Binary Search (`2`) if the entered array is sorted.
- Wrapping `case 2` in `{ ... }` is required in C++ when declaring local
  variables (`low`, `high`, `mid`) inside a `switch` case.
