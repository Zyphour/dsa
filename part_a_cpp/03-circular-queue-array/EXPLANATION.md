# Code explanation — `circular_queue.cpp`

Fixed-size circular queue using `#define SIZE 5`:

```cpp
class CircularQueue {
    int arr[SIZE];
    int front, rear, count;
};
```

Initialised with `front = 0`, `rear = -1`, `count = 0`.

## What each function does

| Function | Job |
|---|---|
| `enqueue(x)` | if `count == SIZE` print full; else `rear = (rear + 1) % SIZE`, `arr[rear] = x`, `count++` |
| `dequeue()` | if `count == 0` print empty; else print `arr[front]`, `front = (front + 1) % SIZE`, `count--` |
| `display()` | if `count == 0` print empty; else print `arr[(front + i) % SIZE]` for `i = 0..count-1` |

## Dry run (SIZE = 5)

| Operation | front | rear | count | Array |
|---|---|---|---|---|
| enqueue 10 | 0 | 0 | 1 | `[10, _, _, _, _]` |
| enqueue 20 | 0 | 1 | 2 | `[10, 20, _, _, _]` |
| enqueue 30 | 0 | 2 | 3 | `[10, 20, 30, _, _]` |
| dequeue → 10 | 1 | 2 | 2 | `[_, 20, 30, _, _]` |
| dequeue → 20 | 2 | 2 | 1 | `[_, _, 30, _, _]` |
| enqueue 40 | 2 | 3 | 2 | `[_, _, 30, 40, _]` |
| enqueue 50 | 2 | 4 | 3 | `[_, _, 30, 40, 50]` |
| enqueue 60 | 2 | **0** | 4 | `[60, _, 30, 40, 50]` ← wrapped |

## Common mistakes

- Checking `rear == SIZE` instead of `count == SIZE` for full.
- Forgetting `% SIZE` when advancing `front` or `rear`.
- Looping `front..rear` directly instead of `(front + i) % SIZE` for `count` steps.

## Viva — short answers

| Question | Answer |
|---|---|
| Why circular instead of linear? | Reuses freed slots at the beginning without O(n) shifting. |
| Full condition without `count`? | `(rear + 1) % SIZE == front` (leaves one slot empty). |
| Time of enqueue / dequeue? | O(1) for both. |
| Real applications? | CPU round-robin scheduling, printer spooler, keyboard buffer. |
