# Practical 6 — Heap Sort

**Aim:** Sort an array of integers in ascending order with Heap Sort, in
`O(n log n)` time and `O(1)` extra space, showing how the heap works.

**Language:** Python · **Program:** [`heap_sort.py`](heap_sort.py)

---

## Concepts

A **heap** is a **complete binary tree** kept inside a plain array — no pointers.
For a **max-heap** every parent is `>=` its children, so the biggest value is
always at index 0.

Because the tree is complete, the positions follow simple formulas:

| Relation | Index |
|---|---|
| parent of `i` | `(i − 1) // 2` |
| left child of `i` | `2i + 1` |
| right child of `i` | `2i + 2` |

```
array:  [ 50, 30, 70, 20, 40, 60, 80 ]
index:     0   1   2   3   4   5   6

            50
          /    \
        30      70
       /  \    /  \
      20  40  60  80
```

**heapify (sift down).** If a node is smaller than one of its children, swap it
with the **larger** child and continue downwards. It travels one path only, so it
costs `O(log n)`.

## The algorithm

**Phase 1 — build a max-heap.** Run `heapify` on every parent, from the last
parent `n//2 − 1` down to index 0. This is `O(n)`, not `O(n log n)`, because most
nodes are near the bottom and barely move.

**Phase 2 — sort.** Swap `arr[0]` (the maximum) with the last element of the heap,
shrink the heap by one, and heapify the new root. Repeat until one element is
left. The sorted part grows at the end of the same array.

```
[4, 10, 3, 5, 1] → build → [10, 5, 3, 4, 1]
swap 10 to the end → [1, 5, 3, 4 | 10] → heapify → [5, 4, 3, 1 | 10]
... → [1, 3, 4, 5, 10]
```

## Complexity

| Phase | Time |
|---|---|
| Build max-heap | O(n) |
| n × heapify | O(n log n) |
| **Total** | **O(n log n)** in best, average and worst case |
| Extra space | O(1) — in place |

Heap sort is **not stable**: long-distance swaps can change the order of equal
values.

## Exam points

- A **min**-heap gives descending output; a max-heap gives ascending.
- Build from the last parent down to 0, not the other way round.
- After each swap the heap size must shrink, otherwise the sorted tail is
  disturbed again.
- Advantages over merge sort: no extra array. Over quick sort: no bad-pivot worst case.
- Used where memory is tight (embedded systems) and to implement priority queues.
