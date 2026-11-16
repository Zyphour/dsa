# Code explanation — `heap_sort.py`

Two functions and a self-check:

| Function | Job |
|---|---|
| `heapify(arr, n, i, trace)` | push `arr[i]` down until the subtree rooted at `i` is a max-heap |
| `heap_sort(arr, trace)` | build the heap, then move the maximum to the end n−1 times |
| `check()` | sorts 60 random arrays and compares with Python's `sorted()` |

## heapify — 8 lines that do the work

```python
largest = i
left, right = 2*i + 1, 2*i + 2

if left  < n and arr[left]  > arr[largest]: largest = left
if right < n and arr[right] > arr[largest]: largest = right

if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest, trace)      # keep going down
```

`n` is the heap size, which shrinks during the sort — that is what keeps the
already sorted tail out of the way.

## heap_sort — two phases

```python
for i in range(n // 2 - 1, -1, -1):      # phase 1: build (last parent -> root)
    heapify(arr, n, i, trace)

for end in range(n - 1, 0, -1):          # phase 2: sort
    arr[0], arr[end] = arr[end], arr[0]  # biggest goes to the end
    heapify(arr, end, 0, trace)          # repair the smaller heap
```

## Trace printed by the program for `[4, 10, 3, 5, 1]`

```
build:            [10, 5, 3, 4, 1]
place 10 at end:  [1, 5, 3, 4 | 10]  -> heapify  [5, 4, 3, 1 | 10]
place 5  at end:  [1, 4, 3 | 5, 10]  -> heapify  [4, 1, 3 | 5, 10]
place 4  at end:  [3, 1 | 4, 5, 10]  -> heapify  [3, 1 | 4, 5, 10]
place 3  at end:  [1 | 3, 4, 5, 10]
sorted:           [1, 3, 4, 5, 10]
```

The `|` marks the growing sorted part at the end of the array — the heap never
touches it again.

## Common mistakes

- Building a min-heap and expecting ascending order.
- Running the build loop from 0 to `n−1` (leaves would be heapified first — harmless
  but pointless — while real parents are skipped).
- Recursing on `i` instead of the swapped child index (`largest`).
- Not shrinking `n` after each swap, so the sorted part gets mixed back in.
- Forgetting the bounds checks `left < n`, `right < n`.
- Claiming heap sort is stable.

## Viva — short answers

| Question | Answer |
|---|---|
| Why O(n log n) even in the worst case? | heapify is O(log n) and is called n times, always. |
| Advantage over merge sort? | O(1) extra space (in place). |
| Advantage over quick sort? | Guaranteed O(n log n), no bad pivot. |
| What is a priority queue? | "Highest priority out first" — implemented with a heap. |
| Is it stable? | No. |
