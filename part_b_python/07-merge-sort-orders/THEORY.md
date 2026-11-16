# Practical 7 — Merge Sort (Online Orders by Delivery Time)

**Aim:** Sort a list of online orders by estimated delivery time using Merge
Sort, so the delivery system handles the quickest orders first.

**Language:** Python · **Program:** [`merge_sort_orders.py`](merge_sort_orders.py)

---

## Concepts

**Divide and conquer** means: split the problem into smaller pieces of the same
kind, solve them with the same function, then combine the answers.

**Merge sort** applies it in three steps:

1. **Divide** — split the list into two halves.
2. **Conquer** — sort each half recursively.
3. **Combine** — merge the two sorted halves into one sorted list.

Base case: a list of 0 or 1 elements is already sorted.

**Merging** two sorted lists: keep a finger at the front of each list, copy the
smaller value into the result, advance that finger, and when one list ends copy
the rest of the other.

```
left  = [10, 25, 30]      right = [15, 20, 90]
take 10 (10<15), 15 (25>15), 20, 25, 30, then 90  ->  [10, 15, 20, 25, 30, 90]
```

Using `<=` in the comparison makes the sort **stable**: orders with the same
delivery time keep their original order.

## Why O(n log n)

Splitting in half creates `log2 n` levels (8 items → 3 levels). At every level the
merging work adds up to `n` comparisons.

```
n × log2 n
1,000 orders : ~10,000 comparisons
1,000 orders with bubble sort : ~5,00,000 comparisons
```

| Sort | Best | Worst | Extra space | Stable |
|---|---|---|---|---|
| Merge sort | O(n log n) | O(n log n) | O(n) | yes |
| Heap sort | O(n log n) | O(n log n) | O(1) | no |
| Bubble sort | O(n) | O(n²) | O(1) | yes |

## Exam points

- Merge sort never beats `O(n log n)`, even on sorted input — it does not check.
- It needs `O(n)` extra memory for the temporary lists, so it is **not in-place**.
- It is ideal for linked lists and for external sorting (files too big for RAM),
  because merging only reads sequentially.
- Key choice matters: sorting by `minutes` puts the fastest delivery first.
- Stability is why object sorts (Java `Arrays.sort`, Python's Timsort) are
  merge-sort based.
