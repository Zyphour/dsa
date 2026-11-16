# Practical 7: Merge Sort — Complete Reference & Code Guide (`merge_sort_orders.py`)

> **Aim:** Sort a list in ascending order using recursive Divide-and-Conquer Merge Sort.
>
> **Language:** Python · **Program:** [`merge_sort_orders.py`](merge_sort_orders.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`merge_sort_orders.py`](merge_sort_orders.py) defines a recursive `merge_sort(a)` function and runs it on the hardcoded list `[8, 3, 5, 1, 9, 2]` to sort and print the numbers in **ascending order**:
1. **Base case:** Returns the list immediately if its length is `0` or `1` (`len(a) <= 1`).
2. **Divide & Conquer:** Splits the list in half at `mid = len(a) // 2` and recursively sorts `left = merge_sort(a[:mid])` and `right = merge_sort(a[mid:])`.
3. **Merge:** Walks two indices `i` and `j` across `left` and `right`, appending the smaller element at each step into `result`, appends any remaining elements from `left[i:]` and `right[j:]`, and prints the final sorted list.

### Exact Program Output
```text
[1, 2, 3, 5, 8, 9]
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Definition |
|---|---|
| **Merge Sort** | A comparison-based, **stable**, **Divide-and-Conquer** sorting algorithm that recursively divides a list into halves until sublists have size `1`, then repeatedly **merges** pairs of sorted sublists into larger sorted lists. |
| **Divide and Conquer** | A 3-stage algorithm design paradigm: **(1) Divide** problem into smaller subproblems, **(2) Conquer** subproblems recursively, **(3) Combine** subproblem solutions into the final answer. |
| **Base Case** | The terminating condition of recursion (`len(a) <= 1`), preventing infinite recursive calls. |
| **Two-Pointer Merge** | Linear `O(n)` procedure using indices `i` (on `left`) and `j` (on `right`) to combine two already-sorted lists into one sorted list. |
| **Stable Sorting Algorithm** | Preserves the original relative order of equal keys (`left[i] <= right[j]` picks `left[i]` first on ties). |
| **Out-of-Place Sorting** | Requires extra auxiliary memory proportional to input size (**`O(n)`** extra space for `result` / slice lists), rather than sorting strictly inside the original array. |
| **External Sorting** | Sorting huge datasets stored on disk/SSD that are too large to fit inside **RAM** (*Random Access Memory*) at once — Merge Sort is the standard algorithm for external sorting. |

---

## 3. Core Facts, Properties, Advantages & Uses

### Key Properties of Merge Sort
- **Paradigm:** Divide and Conquer.
- **Recurrence Relation:** $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$.
- **Time Complexity:** Guaranteed **`O(n log n)`** in **Best, Average, AND Worst** cases (`log₂ n` split levels × `O(n)` merge work per level).
- **Auxiliary Space Complexity:** **`O(n)`** for arrays (plus `O(log n)` recursion call stack) → **NOT in-place** on arrays.
- **Stable?** **Yes** (`<=` in `if left[i] <= right[j]:`).

### Advantages & Disadvantages
- **Advantages:**
  1. **Guaranteed `O(n log n)` worst-case time** — never degrades to `O(n²)` regardless of input order.
  2. **Stable** sort (preserves order of equal records, e.g., e-commerce orders sharing the same delivery time).
  3. Ideal for **Linked Lists** (merges nodes by relinking pointers in `O(1)` extra space) and **External Disk Sorting**.
- **Disadvantages:**
  1. Requires **`O(n)` extra memory** when sorting arrays (unlike Heap Sort's `O(1)`).
  2. Recursive function-call and array-copy overhead makes it slower than Insertion Sort on tiny arrays (`n < 16`).

### Uses / Applications of Merge Sort
1. Sorting **e-commerce / database records stably** (e.g., sorting online orders by delivery ETA while keeping earlier timestamps first on ties).
2. Sorting **Singly and Doubly Linked Lists** (`O(n log n)` time, `O(1)` auxiliary space).
3. **External Sorting** of multi-gigabyte files on disk/databases (`k`-way Merge Sort).
4. Core engine inside **Timsort** (Python's `list.sort()` / `sorted()` and Java's `Arrays.sort()` for objects) and counting **array inversions**.

---

## 4. Step-by-Step Algorithm

1. If `len(a) <= 1`, return `a` (base case).
2. Compute midpoint `mid = len(a) // 2`.
3. Recursively sort left half: `left = merge_sort(a[:mid])`.
4. Recursively sort right half: `right = merge_sort(a[mid:])`.
5. Set `result = []`, `i = 0`, `j = 0`.
6. While `i < len(left)` and `j < len(right)`:
   - If `left[i] <= right[j]`, append `left[i]` to `result` and set `i += 1`.
   - Else append `right[j]` to `result` and set `j += 1`.
7. Append remaining elements `left[i:]` and `right[j:]` to `result`.
8. Return `result`.

---

## 5. Line-by-Line Code Explanation

```python
def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort([8, 3, 5, 1, 9, 2]))
```

| Line(s) | Exact Role in the Program |
|---|---|
| `if len(a) <= 1: return a` | Recursion base case: any empty or 1-element list is already sorted. |
| `mid = len(a) // 2` | Integer floor division computing the middle split index. |
| `left = merge_sort(a[:mid])` | Slices left half `a[0 .. mid - 1]` and recursively sorts it. |
| `right = merge_sort(a[mid:])` | Slices right half `a[mid .. end]` and recursively sorts it. |
| `result = []; i = j = 0` | Prepares merged output list and initializes pointers `i` (into `left`) and `j` (into `right`). |
| `while i < len(left) and j < len(right):` | Compares front unmerged elements while both halves still have items left. |
| `if left[i] <= right[j]: ...` | Appends smaller item (`<=` picks `left[i]` on ties to ensure **stability**) and advances its pointer. |
| `result += left[i:]; result += right[j:]` | Appends leftover elements from whichever half did not finish inside the `while` loop. |

---

## 6. Step-by-Step Dry Run on `[8, 3, 5, 1, 9, 2]`

1. **Divide down to base cases:**
   - Left half `[8, 3, 5]` → `[8]` and `[3, 5]` (`[3]` + `[5]` merge to `[3, 5]`) → merges `[8]` + `[3, 5]` into **`left = [3, 5, 8]`**.
   - Right half `[1, 9, 2]` → `[1]` and `[9, 2]` (`[9]` + `[2]` merge to `[2, 9]`) → merges `[1]` + `[2, 9]` into **`right = [1, 2, 9]`**.
2. **Final Merge of `left = [3, 5, 8]` and `right = [1, 2, 9]`:**
   - `3 vs 1` → append `1` (`j=1`)
   - `3 vs 2` → append `2` (`j=2`)
   - `3 vs 9` → append `3` (`i=1`)
   - `5 vs 9` → append `5` (`i=2`)
   - `8 vs 9` → append `8` (`i=3`, `left` exhausted → exit `while`)
   - Leftovers: `left[3:] = []`, `right[2:] = [9]` → append `9` → **`[1, 2, 3, 5, 8, 9]`**.

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet

| Metric | Complexity | Reason |
|---|---|---|
| **Best-Case Time Complexity** | **O(n log n)** | Always divides into `log₂ n` levels and merges `n` items per level. |
| **Average-Case Time Complexity** | **O(n log n)** | `T(n) = 2T(n/2) + O(n)`. |
| **Worst-Case Time Complexity** | **O(n log n)** | Input order never causes unbalanced splits. |
| **Auxiliary Space Complexity** | **O(n)** | Temporary merged lists of total size `n` (plus `O(log n)` recursion stack). |
| **In-Place (Arrays)? / Stable?** | **No / Yes** | Out-of-place on arrays; strictly stable. |

### Comparison: Merge Sort vs. Heap Sort

| Parameter | Merge Sort | Heap Sort |
|---|---|---|
| **Time (Best / Avg / Worst)** | **O(n log n)** in all cases | **O(n log n)** in all cases |
| **Auxiliary Space** | **O(n)** | **O(1)** (in-place) |
| **Stable?** | **Yes** | **No** |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Omitting `result += left[i:]` and `result += right[j:]`:** Drops the largest remaining element(s) after one half reaches its end.
- **Mistake 2 — Omitting `if len(a) <= 1: return a`:** Triggers infinite recursion (`RecursionError`).
- **Mistake 3 — Using `<` instead of `<=` in `left[i] <= right[j]`:** Breaks stability on duplicate elements.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define Merge Sort and name its algorithmic paradigm. | Merge Sort is a **Divide-and-Conquer** sorting algorithm that recursively splits an array in half, sorts both halves, and merges the two sorted halves in `O(n)` time. |
| 2 | State the best, average, and worst-case time complexities of Merge Sort. | **O(n log n)** in all three cases (Best, Average, and Worst). |
| 3 | State the auxiliary space complexity of Merge Sort on arrays. | **O(n)** auxiliary space (plus `O(log n)` call-stack space). |
| 4 | Is Merge Sort in-place? Is it stable? | **Not in-place** on arrays (`O(n)` extra space), and **Yes, it is stable**. |
| 5 | Write the recurrence relation for Merge Sort. | **$T(n) = 2T(n/2) + O(n)$**, with base case $T(1) = O(1)$. |
| 6 | Why does Merge Sort always achieve `O(n log n)` even in the worst case? | Because it always divides the list at the exact midpoint `n // 2` (`log₂ n` levels), regardless of how the input numbers are arranged. |
| 7 | What is the time complexity of merging two already-sorted lists of sizes `p` and `q`? | **O(p + q)** linear time (at most `p + q - 1` comparisons). |
| 8 | Why do we need `result += left[i:]` and `result += right[j:]` after the `while` loop? | The `while` loop terminates as soon as one half finishes, leaving uncopied larger sorted elements in the other half. |
| 9 | Why is Merge Sort preferred for sorting Linked Lists and External Disk Files? | On linked lists, merging relinks pointers in `O(1)` extra space; on disk files, Merge Sort reads and writes data sequentially in chunks without needing random access. |
| 10 | Give three applications/uses of Merge Sort. | (1) Stable record sorting (orders/databases), (2) sorting linked lists, and (3) external sorting of huge files on disk. |
| 11 | What is the full form of RAM? | **Random Access Memory**. |
| 12 | Which line in the code guarantees stability? | `if left[i] <= right[j]:` — the `<=` operator picks the left element first when two elements are equal. |
