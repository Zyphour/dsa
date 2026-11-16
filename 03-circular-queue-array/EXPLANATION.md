# Student Guide — `circular_queue.cpp`

This guide explains how [`circular_queue.cpp`](circular_queue.cpp) works and prepares you for viva questions.

## How the Code Works

- `int q[5], f = -1, r = -1;` — `q` holds up to 5 integers; `-1` means the queue is currently empty.
- **`enqueue(int x)`:**
  - `(r + 1) % 5 == f` checks if advancing `r` by 1 (wrapping from `4` back to `0`) collides with `f`. If yes, all 5 slots are full.
  - `if (f == -1) f = 0;` handles the very first insertion so `f` points to index `0`.
  - `r = (r + 1) % 5; q[r] = x;` moves rear circularly and stores `x`.
- **`dequeue()`:**
  - `if (f == -1)` catches underflow (empty queue).
  - `if (f == r) f = r = -1;` is super important: when the **last remaining item** is removed, resetting both `f` and `r` to `-1` marks the queue empty again.
  - Otherwise `f = (f + 1) % 5;` moves front one slot forward (wrapping around if needed).
- **`display()`:**
  - Uses an infinite-style loop `for (int i = f; ; i = (i + 1) % 5)` with `if (i == r) break;` at the bottom so it works whether `f <= r` or `r < f` (wrapped around!), and also works when `f == r` (1 element).

## Dry Run

Start: `f = -1, r = -1`
1. `enqueue(10)` → `f = 0, r = 0`, `q[0] = 10`
2. `enqueue(20)` → `f = 0, r = 1`, `q[1] = 20`
3. `enqueue(30), enqueue(40), enqueue(50)` → `f = 0, r = 4` (queue full!)
4. `enqueue(60)` → `(4 + 1) % 5 == 0 == f` → prints `Full`
5. `dequeue()` → prints `Deleted: 10`, `f = 1, r = 4`
6. `enqueue(60)` → `(4 + 1) % 5 = 0 != 1`, so `r = 0`, `q[0] = 60`! (Slot 0 reused!)

## Common Mistakes

- Using `r == 4` as the full check instead of `(r + 1) % 5 == f` — that breaks circular reuse!
- Forgetting `if (f == r) f = r = -1` in `dequeue()` — makes the queue look non-empty even after removing everything.
- Writing `for (int i = f; i <= r; i++)` in `display()` — fails as soon as `r` wraps around before `f` (`r < f`).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| What problem does a Circular Queue solve over a linear array queue? | It reuses empty slots freed at the front of the array instead of reporting "Full" prematurely. |
| What is the full condition and empty condition here? | Empty: `f == -1`. Full: `(r + 1) % SIZE == f`. |
| Why do we use `% 5`? | Modulo wraps index `4 + 1 = 5` back to `0` (`5 % 5 == 0`). |
| Time complexity of `enqueue` and `dequeue`? | `O(1)` — no shifting of elements is needed. |
