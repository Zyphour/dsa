# Linear Search

**Aim:** Search for a target value in an array by checking each element from
start to end.

**Language:** C++ · **Program:** [`linear_search.cpp`](linear_search.cpp)

---

## Concepts

- **Linear (sequential) search** – start at index `0` and compare one element at
  a time until the target is found or the array ends.
- **No prerequisite** – works on both sorted and unsorted arrays.

## Algorithm

1. Read 5 elements into `a[5]` and the target `key`.
2. For `i = 0` to `4`:
   - If `a[i] == key`, print position `i + 1` and exit.
3. If the loop finishes without a match, print `"Not Found"`.

## Comparison

| | Linear Search | Binary Search |
|---|---|---|
| Input order | any (sorted or unsorted) | must be sorted |
| Best case | O(1) | O(1) |
| Worst case | O(n) | O(log n) |
| Space | O(1) | O(1) |

## Exam points

- Returns the **first** occurrence when duplicates exist.
- `i + 1` converts 0-based array index to 1-based human position.
- Best choice for tiny or unsorted arrays.
