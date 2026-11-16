# Practical 3 — Circular Queue using an Array

**Aim:** Implement a circular queue of fixed size with Enqueue, Dequeue and
Display, and handle the queue-full condition.

**Language:** C++ · **Program:** [`circular_queue.cpp`](circular_queue.cpp)

---

## Concepts

**Queue** – a FIFO list: the first element inserted is the first removed.
`enqueue` adds at the **rear**, `dequeue` removes from the **front**.

**Problem with a simple array queue.** Both `front` and `rear` only move forward,
so after a few deletions the free slots at the beginning can never be used again:

```
[ _ _ 30 40 50 ]   front = 2, rear = 4 -> "full", but slots 0 and 1 are empty
```

Shifting everything left on every delete costs `O(n)`. The fix is to wrap around.

**Circular queue.** After the last index we return to 0 using the modulus:

```
rear  = (rear  + 1) % SIZE
front = (front + 1) % SIZE

     +-----+-----+-----+-----+-----+
     | 70  | 80  | 30  | 40  | 50  |      SIZE = 5
     +-----+-----+-----+-----+-----+
        ^rear          ^front
```

Display cannot simply loop `front..rear`, because the queue may be wrapped. It
loops `count` times over `(front + i) % SIZE`.

## Full and empty

Keeping a `count` makes the conditions exact and loses no slot:

| State | Condition |
|---|---|
| empty | `count == 0` |
| full | `count == SIZE` |

Without `count`, the usual trick is to keep one slot empty and test
`(rear + 1) % SIZE == front` — but then a size-n array holds only `n−1` items.

## Complexity

| Operation | Time |
|---|---|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek | O(1) |
| Display | O(n) |

Space: `O(SIZE)` — fixed, no extra allocation.

## Exam points

- Test `count`, not `rear == SIZE`, for the full condition.
- Every index update needs `% SIZE`; forgetting it runs past the array.
- `peek` reads the front without deleting it.
- Uses: printer spooler, keyboard buffer, CPU round-robin scheduling, BFS queue.
