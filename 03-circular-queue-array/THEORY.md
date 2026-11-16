# Practical 3 — Circular Queue on an Array

**Aim:** Implement a fixed-size Circular Queue (`SIZE = 5`) using an array with
`enqueue`, `dequeue`, and `display` operations.

**Language:** C++ · **Program:** [`circular_queue.cpp`](circular_queue.cpp)

---

## Concepts

- **Queue** – FIFO (First In, First Out): insertions happen at the **rear**
  (`r`), deletions happen at the **front** (`f`).
- **Why circular?** In a normal linear array queue, once `r` reaches the last
  index (`4`), you cannot insert even if front slots were freed by `dequeue()`.
  Using `% 5` wraps `4 + 1` back to `0` so freed space is reused.

| Condition | Expression | Meaning |
|---|---|---|
| Empty | `f == -1` | No elements in queue |
| Full | `(r + 1) % 5 == f` | Next slot after `r` wraps onto `f` |
| Last item deleted | `f == r` | Reset `f = r = -1` |

## Algorithm

### `enqueue(x)`
1. If `(r + 1) % 5 == f`, print `"Full"` and return.
2. If `f == -1`, set `f = 0`.
3. Set `r = (r + 1) % 5`, `q[r] = x`.

### `dequeue()`
1. If `f == -1`, print `"Empty"` and return.
2. Print `q[f]`.
3. If `f == r`, set `f = r = -1`; else set `f = (f + 1) % 5`.

## Comparison

| | Linear Array Queue | Circular Queue |
|---|---|---|
| Reuses freed front slots? | No | Yes (via `% SIZE`) |
| `enqueue` / `dequeue` time | O(1) | O(1) |
| Space | O(SIZE) | O(SIZE) |

## Exam points

- `enqueue` and `dequeue` are both **O(1)** — no element shifting is needed.
- Always reset `f = r = -1` when removing the single remaining element (`f == r`).
- `display()` must step using `(i + 1) % 5` until `i == r` because `r` can be
  smaller than `f` after wrap-around.
