# Insertion Sort — Complete Reference & Code Guide (`insertion_sort.cpp`)

> **Aim:** Sort 5 integers in ascending order using Insertion Sort.
>
> **Language:** C++ · **Program:** [`insertion_sort.cpp`](insertion_sort.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`insertion_sort.cpp`](insertion_sort.cpp) reads **5 integers** from the user into an array `a[5]` and sorts them **in place in ascending order** using Insertion Sort. Starting from index `i = 1` up to `i = 4`, it saves `key = a[i]`, shifts every larger element in the sorted left prefix `a[0 .. i - 1]` one slot to the right (`a[j + 1] = a[j]`), inserts `key` into the resulting open slot (`a[j + 1] = key`), and prints the sorted array.

### Sample Run
```text
Enter 5 elements: 9 5 1 4 3
Sorted array: 1 3 4 5 9 
```

---

## 2. Definitions & Key Terminology

| Term | Definition |
|---|---|
| **Insertion Sort** | An in-place, stable comparison-based sorting algorithm that builds the final sorted array one item at a time by taking each element `key = a[i]` and inserting it into its proper position inside the already-sorted prefix `a[0 .. i - 1]`. |
| **Shift Operation** | Moving an element one index to the right (`a[j + 1] = a[j]`) — requires **1 assignment**, compared to **3 assignments** for a full swap. |
| **Adaptive Sorting Algorithm** | A sorting algorithm that runs faster when the input is already partially or fully sorted. Insertion Sort adapts from `O(n²)` down to **`O(n)`** on sorted data. |
| **Online Algorithm** | An algorithm that can process input elements sequentially **as they arrive one by one**, without needing the entire dataset in memory beforehand. |
| **Stable Sort** | Preserves the original relative order of equal keys (`a[j] <= key` stops shifting). |
| **Short-Circuit Evaluation** | Left-to-right evaluation of logical `&&` in C++: if the left side (`j >= 0`) is `false`, the right side (`a[j] > key`) is **not evaluated**, preventing out-of-bounds access `a[-1]`. |

---

## 3. Core Facts, Properties, Advantages & Uses

### Key Properties of Insertion Sort
- **Method:** Comparison-based, Insertion & Right-Shift sort.
- **In-Place?** **Yes** — uses **O(1)** extra space (`key`, `i`, `j`).
- **Stable?** **Yes** — shifting stops as soon as `a[j] <= key`, so equal elements never cross each other.
- **Adaptive?** **Yes** — achieves **O(n)** best-case time on already-sorted arrays (`0` shifts, `n - 1` comparisons).
- **Online?** **Yes** — can maintain a sorted list incrementally as new numbers stream in.

### Advantages & Disadvantages
- **Advantages:**
  1. **Fastest elementary `O(n²)` sort** in practice on small arrays and **nearly-sorted arrays** (`O(n)` best case).
  2. Uses **1-assignment shifts** instead of 3-assignment swaps.
  3. **Stable**, **in-place (`O(1)` extra space)**, and **online**.
- **Disadvantages:**
  1. Degrades to **O(n²)** comparisons and shifts on random or reverse-sorted large datasets.

### Uses / Applications of Insertion Sort
1. Sorting **nearly-sorted** or **almost-sorted** datasets in near-linear `O(n)` time.
2. Sorting **small subarrays (`n <= 16..32`)** inside industrial hybrid sorts such as **Timsort** (Python's `sort()`) and **Introsort** (C++ `std::sort`).
3. **Online / streaming insertion** — maintaining a live leaderboard or sorted list as elements arrive one at a time.

---

## 4. Step-by-Step Algorithm

1. Start.
2. Read 5 integers into `a[0 .. 4]`.
3. **Outer loop:** For `i = 1` to `4` (index `0` alone is already a sorted 1-element prefix):
   - Set `key = a[i]` and `j = i - 1`.
   - **Inner `while` loop:** While `j >= 0` **and** `a[j] > key`:
     - Shift element right: `a[j + 1] = a[j]`.
     - Decrement `j = j - 1`.
   - Insert `key` at the open position: `a[j + 1] = key`.
4. Print `a[0 .. 4]`.
5. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int main() {
    int a[5], key, j;
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) cin >> a[i];
    for (int i = 1; i < 5; i++) {
        key = a[i]; j = i - 1;
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
        a[j + 1] = key;
    }
    cout << "Sorted array: ";
    for (int i = 0; i < 5; i++) cout << a[i] << " ";
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `int a[5], key, j;` | Declares 5-element array `a`, `key` (element currently being inserted), and backward scan index `j`. |
| `for (int i = 0; i < 5; i++) cin >> a[i];` | Reads 5 integers from the keyboard into `a[0 .. 4]`. |
| `for (int i = 1; i < 5; i++)` | Starts at `i = 1` because `a[0]` is a 1-element sorted prefix. |
| `key = a[i]; j = i - 1;` | Saves `a[i]` in `key` before shifting overwrites `a[i]`, and starts scanning leftward from `i - 1`. |
| `while (j >= 0 && a[j] > key)` | Checks `j >= 0` **first** (preventing `a[-1]` out-of-bounds read), then checks if `a[j]` is strictly greater than `key`. |
| `{ a[j + 1] = a[j]; j--; }` | Copies `a[j]` one position right and steps `j` one index left. |
| `a[j + 1] = key;` | Places `key` into index `j + 1` (the slot vacated after `j` stopped at `-1` or at an element `<= key`). |
| `for (int i = 0; i < 5; i++) cout << a[i] << " ";` | Outputs the final sorted 5 integers. |

---

## 6. Step-by-Step Dry Run

**Input:** `a = [9, 5, 1, 4, 3]`

| Pass `i` | `key` | Shifts Performed in `while` | Final `j` | Insertion `a[j+1] = key` | Array After Pass (`\|` = sorted prefix) |
|---|---|---|---|---|---|
| Initial | — | — | — | — | `[9 \| 5, 1, 4, 3]` |
| `i = 1` | `5` | `a[1] = 9` (`j → -1`) | `-1` | `a[0] = 5` | `[5, 9 \| 1, 4, 3]` |
| `i = 2` | `1` | `a[2] = 9`, `a[1] = 5` (`j → -1`) | `-1` | `a[0] = 1` | `[1, 5, 9 \| 4, 3]` |
| `i = 3` | `4` | `a[3] = 9`, `a[2] = 5` (stops at `a[0]=1 <= 4`) | `0` | `a[1] = 4` | `[1, 4, 5, 9 \| 3]` |
| `i = 4` | `3` | `a[4] = 9`, `a[3] = 5`, `a[2] = 4` (stops at `a[0]=1 <= 3`) | `0` | `a[1] = 3` | `[1, 3, 4, 5, 9]` |

**Final Output:** `Sorted array: 1 3 4 5 9 `

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet (for `n` elements)

| Case | Input Condition | Comparisons / Shifts | Big-O Complexity |
|---|---|---|---|
| **Best-Case Time** | **Already sorted** (`[1, 2, 3, 4, 5]`) | `n - 1` comparisons, **`0` shifts** | **O(n)** |
| **Average-Case Time** | Random order | `~n² / 4` comparisons & shifts | **O(n²)** |
| **Worst-Case Time** | **Reverse sorted** (`[5, 4, 3, 2, 1]`) | `1 + 2 + ... + (n - 1) = n(n - 1) / 2` | **O(n²)** |
| **Auxiliary Space Complexity** | In-place (`key`, `i`, `j` only) | Constant memory | **O(1)** |
| **Stable? / Adaptive? / Online?** | — | — | **Yes / Yes / Yes** |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Reversing condition order `while (a[j] > key && j >= 0)`:** Evaluates `a[-1]` out of bounds before checking `j >= 0`!
- **Mistake 2 — Writing `a[j] = key` instead of `a[j + 1] = key`:** Because `j--` ran at the end of the last shift, the open slot is at `j + 1`, not `j`.
- **Mistake 3 — Using `a[j] >= key` instead of `a[j] > key`:** Shifts equal elements and destroys stability.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define Insertion Sort. | Insertion Sort is an in-place, stable sorting algorithm that iterates from index `1` to `n - 1` and inserts each element `key = a[i]` into its proper position in the sorted prefix `a[0 .. i - 1]` by shifting larger elements right. |
| 2 | State the best, average, and worst-case time complexities of Insertion Sort. | Best case: **O(n)**, Average case: **O(n²)**, Worst case: **O(n²)**. |
| 3 | When do the best case and worst case occur in Insertion Sort? | **Best case:** input is already sorted in ascending order. **Worst case:** input is sorted in reverse (descending) order. |
| 4 | What is the auxiliary space complexity of Insertion Sort? | **O(1)** (constant extra space; sorts in place). |
| 5 | Is Insertion Sort stable? Why? | **Yes**, because the `while` loop shifts elements strictly when `a[j] > key` and stops on `a[j] <= key`, preserving the order of duplicates. |
| 6 | Why does the outer loop start from `i = 1` instead of `i = 0`? | Because the single element `a[0]` by itself is trivially sorted. |
| 7 | Why must `j >= 0` be placed before `a[j] > key` in the `while` condition? | Due to **short-circuit evaluation** of `&&`: if `j` reaches `-1`, `j >= 0` is `false` and prevents reading invalid memory `a[-1]`. |
| 8 | Why is Insertion Sort faster in practice than Bubble Sort on small arrays? | It uses **1-write shifts** (`a[j + 1] = a[j]`) instead of 3-write swaps and stops scanning the prefix immediately as soon as `a[j] <= key`. |
| 9 | What does it mean that Insertion Sort is an **online** and **adaptive** algorithm? | **Online:** it can sort items one by one as they arrive without having the full dataset upfront. **Adaptive:** it runs faster (`O(n)`) when data is nearly sorted. |
| 10 | Give three real-world uses of Insertion Sort. | (1) Sorting nearly-sorted arrays, (2) base-case sorter for small slices inside Python's Timsort and C++'s `std::sort`, and (3) maintaining a live sorted stream of incoming elements. |
| 11 | Why do we write `a[j + 1] = key` instead of `a[j] = key`? | Because the `while` loop decrements `j` one final time before terminating, leaving `j` one index to the left of the vacant slot. |
| 12 | How many shifts occur if the input is `[10, 20, 30, 40, 50]`? | **`0` shifts** (and only `4` comparisons). |
