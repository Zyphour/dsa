# Practical 6 — Heap Sort

**Aim:** Sort an array in ascending order in place using a Max-Heap and the Heap
Sort algorithm.

**Language:** Python · **Program:** [`heap_sort.py`](heap_sort.py)

---

## Concepts

- **Binary Heap (array representation)** – for a node at index `i` (0-based):
  - Left child = `2*i + 1`, right child = `2*i + 2`.
- **Max-Heap property** – every parent is `>=` both of its children, so `a[0]`
  is always the maximum element.
- **Why Max-Heap for ascending sort?** Swapping `a[0]` to the end (`a[i]`)
  places the largest items from right to left.

## Algorithm

### `heapify(a, n, i)`
1. Set `largest = i`, `left = 2*i + 1`, `right = 2*i + 2`.
2. Update `largest` if `left < n` and `a[left] > a[largest]`, or `right < n`
   and `a[right] > a[largest]`.
3. If `largest != i`, swap `a[i]` with `a[largest]` and call `heapify(a, n, largest)`.

### `heap_sort(a)`
1. **Build Max-Heap:** for `i = n // 2 - 1` down to `0`, call `heapify(a, n, i)`.
2. **Extract:** for `i = n - 1` down to `1`, swap `a[0]` and `a[i]`, then call
   `heapify(a, i, 0)`.

## Comparison

| | Heap Sort | Merge Sort | Quick Sort |
|---|---|---|---|
| Best / Avg / Worst | O(n log n) always | O(n log n) always | O(n log n) avg, O(n²) worst |
| Extra space | O(1) in-place | O(n) | O(log n) |
| Stable? | No | Yes | No |

## Exam points

- Building the heap starts at `n // 2 - 1` because indices `n // 2 .. n - 1` are
  leaves with no children.
- Building a heap takes `O(n)` time; `n - 1` extractions take `O(n log n)` total.
- Heap Sort is **not stable** because long swaps reorder equal elements.
