# Code explanation — `circular_queue.cpp`

One class sized by a constant:

```cpp
const int SIZE = 5;      // fixed size of the queue

class CircularQueue {
    int data[SIZE];
    int front;           // index of the first element
    int rear;            // index of the last element
    int count;           // how many elements are inside
};
```

The constructor sets `front = 0`, `rear = -1`, `count = 0`, so the first enqueue
puts the element at index 0.

## What each function does

| Function | Job |
|---|---|
| `isEmpty()` / `isFull()` | `count == 0` / `count == SIZE` |
| `enqueue(value)` | refuse if full; else move rear with `% SIZE`, store, `count++` |
| `dequeue()` | refuse if empty; take `data[front]`, move front with `% SIZE`, `count--` |
| `display()` | loop `count` times over `(front + i) % SIZE`, then draw the array |
| `peek()` | print `data[front]` without removing it |

Key lines:

```cpp
rear = (rear + 1) % SIZE;      // 4 -> 0 : the wrap-around
data[rear] = value;
count++;

front = (front + 1) % SIZE;
count--;
```

and the display walk that follows the wrap:

```cpp
for (int i = 0; i < count; i++) {
    int index = (front + i) % SIZE;
    cout << data[index] << " ";
}
```

`display()` also prints a picture of the array (`[ 30 ]` for used slots,
`[ -- ]` for free ones) so the wrap is visible on screen.

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

Note the last row: `rear` wrapped to 0, so the element lands at the start of the
array while the front is still at index 2.

## Common mistakes

- Testing `rear == SIZE` instead of `count == SIZE` to detect full.
- Forgetting `% SIZE`, so an index runs out of the array.
- Printing `front..rear` in order, which reorders or misses wrapped elements.
- Decrementing `count` on a failed (empty) dequeue.

## Viva — short answers

| Question | Answer |
|---|---|
| Why circular instead of linear? | Free slots at the start get reused; no shifting. |
| Full condition without `count`? | `(rear + 1) % SIZE == front` (one slot stays empty). |
| Time of enqueue/dequeue? | O(1) for both. |
| Real use? | Printer queue, keyboard buffer, round-robin scheduling, BFS. |
