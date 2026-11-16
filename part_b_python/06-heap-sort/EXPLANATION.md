# Code explanation — `heap_sort.py`

28-line program with `heapify`, `heap_sort`, and a sample array `arr = [12, 11, 13, 5, 6, 7]`.

## Functions

| Function | Job |
|---|---|
| `heapify(arr, n, i)` | sifts `arr[i]` down using `l = 2 * i + 1`, `r = 2 * i + 2` until subtree `i` is a max-heap |
| `heap_sort(arr)` | builds max-heap from `n // 2 - 1` down to `0`, then swaps `arr[0]` with `arr[i]` for `i = n - 1` down to `1` |

## Code breakdown

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):    # build max-heap
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):          # extract max one by one
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
```

## Dry run — `[12, 11, 13, 5, 6, 7]`

- Build max-heap → `[13, 11, 12, 5, 6, 7]`
- Swap `13` to index 5, heapify size 5 → `[12, 11, 7, 5, 6 | 13]`
- Swap `12` to index 4, heapify size 4 → `[11, 6, 7, 5 | 12, 13]`
- Continue until sorted → `[5, 6, 7, 11, 12, 13]`

## Viva — short answers

| Question | Answer |
|---|---|
| Worst-case time complexity? | O(n log n) — best, average and worst are all O(n log n). |
| Space complexity? | O(1) auxiliary space (in-place sort). |
| Why start build loop at `n // 2 - 1`? | Indices from `n // 2` onwards are leaf nodes and already valid 1-node heaps. |
| Is heap sort stable? | No. |
