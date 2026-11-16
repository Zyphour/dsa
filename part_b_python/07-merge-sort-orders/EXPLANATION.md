# Code explanation — `merge_sort_orders.py`

Sorts 5 online order dictionaries by `"minutes"` in ascending order.

## Functions

| Function | Job |
|---|---|
| `merge(left, right)` | merges two sorted halves using `<=` on `"minutes"`, then appends remaining elements with `extend` |
| `merge_sort(arr)` | base case `len(arr) <= 1`, splits at `mid = len(arr) // 2`, recursively sorts and merges |

## Code breakdown

```python
def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["minutes"] <= right[j]["minutes"]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
```

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
```

## Dry run

Input times `[45, 20, 15, 30, 10]`:
- Split `[45, 20]` and `[15, 30, 10]`
- Left sorts to `[20, 45]`; right sorts to `[10, 15, 30]`
- `merge` combines them → `[10, 15, 20, 30, 45]` (`Mug`, `Bottle`, `Book`, `Charger`, `Bag`)

## Viva — short answers

| Question | Answer |
|---|---|
| Time complexity? | O(n log n) in best, average and worst case. |
| Space complexity? | O(n) extra space for merged lists. |
| Why is `<=` used instead of `<`? | Keeps equal delivery times in original arrival order (stability). |
