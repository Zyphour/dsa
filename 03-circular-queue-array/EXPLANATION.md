# Practical 3: Circular Queue on an Array — Complete Reference & Code Guide (`circular_queue.cpp`)

> **Aim:** Implement a fixed-size Circular Queue (`SIZE = 5`) using an array with `enqueue`, `dequeue`, and `display` operations.
>
> **Language:** C++ · **Program:** [`circular_queue.cpp`](circular_queue.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`circular_queue.cpp`](circular_queue.cpp) implements a **Circular Queue of fixed capacity `5`** stored in a global integer array `q[5]` with front index `f = -1` and rear index `r = -1`. It runs a **repeating 4-option menu**:
- **`1. Enqueue`:** Reads an integer `x` and inserts it at the rear (`r = (r + 1) % 5`), wrapping back from index `4` to `0` to reuse freed front slots, or prints `"Full"` if all 5 slots are occupied.
- **`2. Dequeue`:** Removes and prints the front element (`q[f]`), advancing `f = (f + 1) % 5` (or resetting `f = r = -1` when removing the last item), or prints `"Empty"` if the queue is empty.
- **`3. Display`:** Prints all active elements in FIFO order from `f` around to `r`, or `"Empty"` if empty.
- **`4. Exit`:** Terminates the program.

### Sample Run
```text
1.Enqueue 2.Dequeue 3.Display 4.Exit
1 10
1.Enqueue 2.Dequeue 3.Display 4.Exit
1 20
1.Enqueue 2.Dequeue 3.Display 4.Exit
3
10 20 
1.Enqueue 2.Dequeue 3.Display 4.Exit
2
Deleted: 10
1.Enqueue 2.Dequeue 3.Display 4.Exit
4
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **FIFO** | **Full Form:** *First In, First Out* (also called **LILO** = *Last In, Last Out*) — the element inserted earliest is removed earliest. |
| **Queue** | A linear FIFO data structure where insertions occur at one end called **Rear (`r`)** and deletions occur at the opposite end called **Front (`f`)**. |
| **Circular Queue (Ring Buffer)** | A linear queue implemented on a fixed-size array whose last index (`SIZE - 1`) wraps back around to index `0` using modulo arithmetic (`% SIZE`) so vacated front slots can be reused. |
| **Enqueue** | Operation that **inserts** a new element at the **rear** of the queue. |
| **Dequeue** | Operation that **deletes** and returns the oldest element from the **front** of the queue. |
| **Queue Overflow (Full)** | Attempting to `enqueue` when all array slots are occupied (`(r + 1) % SIZE == f`). |
| **Queue Underflow (Empty)** | Attempting to `dequeue` when the queue contains zero elements (`f == -1`). |
| **False Overflow** | Defect of a **simple linear array queue** where `rear == SIZE - 1` reports "Full" even though front indices (`0 .. f - 1`) are empty after earlier `dequeue` operations. |
| **Modulo Operator (`%`)** | Returns the integer remainder of division; `(i + 1) % 5` cycles `0 → 1 → 2 → 3 → 4 → 0`. |
| **CPU** | **Full Form:** *Central Processing Unit* (uses Circular Queues for Round-Robin process scheduling). |

---

## 3. Core Conditions, Formulas, Advantages & Uses

### Essential State Conditions (`SIZE = 5`)

| State / Event | Exact Formula / Code | Meaning |
|---|---|---|
| **Initial / Empty State** | `f == -1` (with `r == -1`) | Queue contains `0` elements. |
| **Full (Overflow) Condition** | `(r + 1) % 5 == f` | Next slot after `r` collides with `f` (all 5 slots full). |
| **First Element Inserted** | `if (f == -1) f = 0;` | Sets both `f = 0` and `r = 0`. |
| **Last Remaining Element Deleted** | `if (f == r) f = r = -1;` | Only 1 item was left; resets queue back to Empty. |
| **Circular Advance** | `r = (r + 1) % 5` / `f = (f + 1) % 5` | Wraps index `4 + 1 = 5` back to `5 % 5 = 0`. |
| **Element Count (when non-empty)** | `(r - f + 5) % 5 + 1` | Number of active items currently stored. |

### Advantages & Disadvantages
- **Advantages:**
  1. **Eliminates False Overflow** — reuses freed front slots completely.
  2. Both `enqueue` and `dequeue` run in **O(1)** constant time with **zero element shifting**.
  3. Predictable, fixed `O(SIZE)` memory footprint with no pointer overhead.
- **Disadvantages:**
  1. Maximum capacity (`SIZE = 5`) is fixed at compile time (unlike a linked-list queue).

### Uses / Applications of Circular Queue
1. **CPU Scheduling (Round-Robin scheduling)** in operating systems.
2. **Memory / I/O Ring Buffers** — keyboard input buffers, audio/video streaming buffers, and network packet queues.
3. **Printer Spoolers** managing print jobs in arrival order.
4. **Traffic light control systems** cycling states repeatedly in a fixed loop.

---

## 4. Step-by-Step Algorithms

### `enqueue(x)`
1. If `(r + 1) % 5 == f`, print `"Full"` and return.
2. If `f == -1`, set `f = 0`.
3. Set `r = (r + 1) % 5` and store `q[r] = x`.

### `dequeue()`
1. If `f == -1`, print `"Empty"` and return.
2. Print `"Deleted: "` followed by `q[f]`.
3. If `f == r`, reset `f = r = -1`; otherwise set `f = (f + 1) % 5`.

### `display()`
1. If `f == -1`, print `"Empty"` and return.
2. Start at `i = f`; print `q[i]`; if `i == r`, stop (`break`); else advance `i = (i + 1) % 5` and repeat.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int q[5], f = -1, r = -1;
void enqueue(int x) {
    if ((r + 1) % 5 == f) cout << "Full";
    else { if (f == -1) f = 0; r = (r + 1) % 5; q[r] = x; }
}
void dequeue() {
    if (f == -1) cout << "Empty";
    else { cout << "Deleted: " << q[f]; if (f == r) f = r = -1; else f = (f + 1) % 5; }
}
void display() {
    if (f == -1) cout << "Empty";
    else {
        for (int i = f; ; i = (i + 1) % 5) { cout << q[i] << " "; if (i == r) break; }
    }
}
int main() {
    int ch, x;
    do {
        cout << "\n1.Enqueue 2.Dequeue 3.Display 4.Exit\n"; cin >> ch;
        switch (ch) {
            case 1: cin >> x; enqueue(x); break;
            case 2: dequeue(); break;
            case 3: display(); break;
        }
    } while (ch != 4);
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `int q[5], f = -1, r = -1;` | Declares 5-element circular buffer `q` and initializes front `f` and rear `r` to `-1` (empty). |
| `if ((r + 1) % 5 == f) cout << "Full";` | Overflow check before insertion. |
| `if (f == -1) f = 0; r = (r + 1) % 5; q[r] = x;` | Initializes `f = 0` on first insertion, wraps `r` circularly, and stores `x`. |
| `if (f == -1) cout << "Empty";` | Underflow check before deletion or display. |
| `if (f == r) f = r = -1; else f = (f + 1) % 5;` | Resets both indices to `-1` if the sole remaining item was deleted; otherwise advances `f` circularly. |
| `for (int i = f; ; i = (i + 1) % 5) { ... if (i == r) break; }` | Prints from `f` around to `r` circularly — works even when `r < f` (wrapped around) or `f == r` (1 item). |
| `do { ... } while (ch != 4);` | Repeats the interactive menu until user enters `4`. |

---

## 6. Step-by-Step Dry Run (Demonstrating Circular Wrap-Around)

| Step | Operation | `(f, r)` Before | `(f, r)` After | Active Queue Slots `q[0..4]` | Printed Output |
|---|---|---|---|---|---|
| 1 | `enqueue(10..50)` (5 calls) | `(-1, -1)` | `(0, 4)` | `[10, 20, 30, 40, 50]` | — |
| 2 | `enqueue(60)` | `(0, 4)` | `(0, 4)` | `(4+1)%5 == 0 == f` | `Full` |
| 3 | `dequeue()` | `(0, 4)` | `(1, 4)` | `[_, 20, 30, 40, 50]` | `Deleted: 10` |
| 4 | **`enqueue(60)`** | `(1, 4)` | **`(1, 0)`** | **`[60, 20, 30, 40, 50]`** *(index `0` reused!)* | — |
| 5 | **`display()`** | `(1, 0)` | `(1, 0)` | Visits `i = 1, 2, 3, 4, 0` | `20 30 40 50 60 ` |

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| **`enqueue(x)`** | **O(1)** | O(1) auxiliary |
| **`dequeue()`** | **O(1)** | O(1) auxiliary |
| **`display()`** | **O(n)** (`n <= SIZE`) | O(1) auxiliary |
| **Overall Data Structure Space** | — | **O(SIZE)** (`5` integers + `f`, `r`) |

### Comparison: Linear Array Queue vs. Circular Queue

| Parameter | Linear Array Queue | Circular Array Queue |
|---|---|---|
| **Reuses vacated front slots?** | **No** (suffers from False Overflow) | **Yes** (via `% SIZE`) |
| **`enqueue` / `dequeue` Time** | O(1) *(or O(n) if shifting)* | **O(1)** (no shifting) |
| **Total Space** | O(SIZE) | **O(SIZE)** |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Checking `r == 4` for Full:** Prevents circular wrap-around; always check `(r + 1) % 5 == f`.
- **Mistake 2 — Omitting `if (f == r) f = r = -1;` in `dequeue()`:** Leaves `f` and `r` pointing inside the array when the queue becomes empty, breaking subsequent `Empty`/`Full` checks.
- **Mistake 3 — Using `for (int i = f; i <= r; i++)` in `display()`:** Fails whenever `r` wraps around to an index smaller than `f` (e.g., `f = 2, r = 0`).

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | What is the full form of FIFO? | **First In, First Out**. |
| 2 | Define a Queue and a Circular Queue. | A **Queue** is a linear FIFO structure with insertions at `rear` and deletions at `front`. A **Circular Queue** connects the last array position back to index `0` using `% SIZE` to reuse freed space. |
| 3 | What are the technical names for insertion and deletion in a Queue? | Insertion is **Enqueue** (at `rear`); deletion is **Dequeue** (at `front`). |
| 4 | What limitation of a simple linear array queue does a Circular Queue overcome? | **False Overflow** (wasted empty slots at the front after `dequeue` operations when `rear` reaches `SIZE - 1`). |
| 5 | State the Empty condition and Full condition of this Circular Queue. | **Empty:** `f == -1`. **Full:** `(r + 1) % SIZE == f`. |
| 6 | State the time complexity of `enqueue` and `dequeue` in a Circular Queue. | Both are **O(1)** constant time. |
| 7 | State the space complexity of a Circular Queue of capacity `SIZE`. | **O(SIZE)** total space and **O(1)** auxiliary space. |
| 8 | Why do we reset `f = r = -1` when `f == r` during `dequeue()`? | Because `f == r` means the last remaining element is being deleted, so the queue must return to the Empty state (`-1`). |
| 9 | What is the role of `% 5` (modulo operator) in `r = (r + 1) % 5`? | When `r` is at the last index `4`, `(4 + 1) % 5 = 0`, wrapping `r` cleanly back to index `0`. |
| 10 | Differentiate between a Stack and a Queue. | **Stack:** LIFO, 1 pointer (`top`) for both push & pop. **Queue:** FIFO, 2 pointers (`rear` for enqueue, `front` for dequeue). |
| 11 | Formula for current number of elements in a non-empty Circular Queue? | `(r - f + SIZE) % SIZE + 1`. |
| 12 | List three real-world uses/applications of Circular Queues. | (1) OS Round-Robin CPU scheduling, (2) audio/network I/O ring buffers, and (3) printer job spooling. |
