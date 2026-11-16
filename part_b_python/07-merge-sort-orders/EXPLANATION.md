# Code explanation — `merge_sort_orders.py`

Each order is a small dictionary, so the delivery time is a named field:

```python
{"id": "ORD-101", "item": "Laptop Bag", "minutes": 45}
```

`ORDERS` holds 12 such orders, and `comparisons` is a counter that proves how much
work the algorithm does.

## What each function does

| Function | Job |
|---|---|
| `merge_sort(orders)` | split in the middle, sort both halves, merge |
| `merge(left, right)` | two-finger merge of two sorted lists, counts comparisons |
| `show(orders, title)` | table print |
| `main` block | unsorted table → sorted table → comparison count → self-check |

## The two functions

```python
def merge_sort(orders):
    if len(orders) <= 1:                     # base case
        return orders

    middle = len(orders) // 2                # DIVIDE
    left  = merge_sort(orders[:middle])
    right = merge_sort(orders[middle:])

    return merge(left, right)                # COMBINE
```

```python
def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i]["minutes"] <= right[j]["minutes"]:   # '<=' keeps it stable
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])                  # copy whatever is left
    result.extend(right[j:])
    return result
```

Slicing (`orders[:middle]`) creates new lists, which is why the original list is
never changed — and why the extra space is `O(n)`.

## Dry run — merging `[20, 45]` and `[15, 30]`

| Step | left finger | right finger | take | result |
|---|---|---|---|---|
| 1 | 20 | 15 | 15 | `[15]` |
| 2 | 20 | 30 | 20 | `[15, 20]` |
| 3 | 45 | 30 | 30 | `[15, 20, 30]` |
| 4 | 45 | — | 45 + leftover | `[15, 20, 30, 45]` |

Full picture for 12 orders: split into 6 + 6, then 3 + 3 + 3 + 3, then pairs,
then merge back up. The output starts with `Coffee Mug (10 min)` and ends with
`Dumbbells (150 min)`.

## Common mistakes

- Forgetting the base case → `RecursionError: maximum recursion depth`.
- Merging without copying the leftover elements of the longer half.
- Using `<` instead of `<=` and then claiming the sort is stable.
- Sorting by `id` instead of `minutes`.
- Saying merge sort is in-place (it needs `O(n)` extra).

## Viva — short answers

| Question | Answer |
|---|---|
| Why O(n log n)? | log n levels of splitting, O(n) merging per level. |
| Best case? | Still O(n log n) — it does not notice sorted input. |
| Why is it stable? | The `<=` comparison takes the left element when the times are equal. |
| Where is it used? | Python/Java object sorting (Timsort), external sorting, linked lists. |
| Merge sort vs heap sort? | Merge is stable but needs O(n) space; heap is in place but unstable. |
