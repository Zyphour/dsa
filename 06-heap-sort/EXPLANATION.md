# Practical 6: Heap Sort — Complete Reference & Code Guide (`heap_sort.py`)

> **Aim:** Sort an array in ascending order in place using a Max-Heap and the Heap Sort algorithm.
>
> **Language:** Python · **Program:** [`heap_sort.py`](heap_sort.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`heap_sort.py`](heap_sort.py) sorts the hardcoded Python list `[4, 10, 3, 5, 1]` **in place in ascending order** using **Heap Sort** and prints the sorted result. It works in two phases:
1. **Build Max-Heap Phase:** Rearranges the list into a valid **Max-Heap** (`[10, 5, 3, 4, 1]`) so the largest element sits at index `0`.
2. **Extract-Max Phase:** Repeatedly swaps the maximum at `a[0]` with the last unsorted position `a[i]` (`i` counting down from `n - 1` to `1`) and calls `heapify(a, i, 0)` on the shrunk heap of size `i` until the entire list is sorted.

### Exact Program Output
```text
[1, 3, 4, 5, 10]
```

---

## 2. Definitions & Key Terminology

| Term / Formula | Definition |
|---|---|
| **Complete Binary Tree** | A binary tree in which every level (except possibly the last) is completely filled, and all nodes in the last level are packed as far **left** as possible (zero index gaps when stored in an array). |
| **Binary Heap** | A **Complete Binary Tree** stored inside an array that satisfies the **Heap Ordering Property** (either Max-Heap or Min-Heap). |
| **Max-Heap** | A Binary Heap where **every parent node is greater than or equal to (`>=`) both of its children**. The **maximum** element is always at the root `a[0]`. |
| **Min-Heap** | A Binary Heap where **every parent node is less than or equal to (`<=`) both of its children**. The **minimum** element is always at the root `a[0]`. |
| **`heapify` (Sift-Down)** | Procedure that restores the Max-Heap property at index `i` (assuming `i`'s left and right subtrees are already valid Max-Heaps) by swapping `a[i]` downward with its larger child in **O(log n)** time. |
| **0-Based Array Heap Formulas** | For node at index `i`: **Left child = `2*i + 1`**, **Right child = `2*i + 2`**, **Parent = `(i - 1) // 2`**. |
| **Leaf vs. Non-Leaf Indices** | For size `n`: **Leaves** sit at indices **`n // 2` to `n - 1`**; **last non-leaf (internal) node** sits at **`n // 2 - 1`**. |

---

## 3. Core Facts, Rules, Advantages & Uses

### Key Heap Sort Facts
1. **Why Ascending Sort Uses a Max-Heap (NOT a Min-Heap):**
   - Swapping root `a[0]` (the maximum) with the end of the active heap `a[i]` places the largest elements from right to left (`n - 1` down to `0`) **in place**, resulting in **ascending** order. *(Using a Min-Heap in place sorts in **descending** order!)*
2. **Why Build-Heap Starts at `n // 2 - 1`:**
   - Elements from `n // 2` to `n - 1` are **leaf nodes** with no children, so they already obey the Max-Heap property trivially.
3. **In-Place & Guaranteed `O(n log n)`:**
   - Unlike Merge Sort (which needs `O(n)` extra array space) and Quick Sort (which degrades to `O(n²)` in the worst case), Heap Sort runs in **O(n log n)** in **Best, Average, AND Worst** cases using **O(1) extra array space**!
4. **Not Stable:** Long-range swaps between `a[0]` and `a[i]` reorder equal keys.

### Advantages & Disadvantages
- **Advantages:**
  1. Guaranteed **O(n log n)** time complexity in **all** cases (no worst-case `O(n²)` trap).
  2. **In-place** sorting (no auxiliary array allocation).
- **Disadvantages:**
  1. **Unstable** sorting algorithm.
  2. Slower constant factor in cache performance than Quick Sort due to jumping between `i` and `2*i + 1`.

### Uses / Applications of Heaps & Heap Sort
1. **In-place sorting with strict worst-case `O(n log n)` guarantees** (embedded, real-time, and security-critical systems; also used as the fallback inside C++ `std::sort` Introsort).
2. Implementing **Priority Queues** (OS process schedulers, Dijkstra's shortest path, Prim's MST, A\* search, Huffman coding).
3. Finding the **`k` largest or `k` smallest elements** in a large stream in `O(n log k)` time.

---

## 4. Step-by-Step Algorithm

### `heapify(a, n, i)`
1. Set `largest = i`, `left = 2 * i + 1`, `right = 2 * i + 2`.
2. If `left < n` and `a[left] > a[largest]`, set `largest = left`.
3. If `right < n` and `a[right] > a[largest]`, set `largest = right`.
4. If `largest != i`, swap `a[i]` with `a[largest]` and recursively call `heapify(a, n, largest)`.

### `heap_sort(a)`
1. Let `n = len(a)`.
2. **Build Max-Heap:** Loop `i` from `n // 2 - 1` down to `0`, calling `heapify(a, n, i)`.
3. **Extract elements:** Loop `i` from `n - 1` down to `1`:
   - Swap `a[0]` and `a[i]`.
   - Call `heapify(a, i, 0)` on the reduced heap of size `i`.
4. Return `a`.

---

## 5. Line-by-Line Code Explanation

```python
def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]: largest = left
    if right < n and a[right] > a[largest]: largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1): heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

print(heap_sort([4, 10, 3, 5, 1]))
```

| Line(s) | Exact Role in the Program |
|---|---|
| `def heapify(a, n, i):` | `n` specifies the **active heap boundary** (`<= len(a)`), and `i` is the subtree root to fix. |
| `left = 2 * i + 1; right = 2 * i + 2` | Computes 0-based left and right child indices of `i`. |
| `if left < n ...` / `if right < n ...` | Ensures child index lies inside the active heap `0 .. n - 1` and finds the largest among parent, left child, and right child. |
| `if largest != i: ... heapify(a, n, largest)` | Swaps parent with larger child and continues sifting down the affected child subtree. |
| `for i in range(n // 2 - 1, -1, -1):` | Bottom-up Build-Heap loop from last non-leaf `n // 2 - 1` down to root `0` (`O(n)` total time). |
| `for i in range(n - 1, 0, -1):` | Extraction loop: swaps max `a[0]` into final sorted slot `a[i]` and re-heapifies prefix `0 .. i - 1` by passing heap size **`i`**. |

---

## 6. Step-by-Step Dry Run on `[4, 10, 3, 5, 1]`

### Phase 1 — Build Max-Heap (`n = 5`, `n // 2 - 1 = 1`)
- `i = 1`: `a[1]=10` > children `5, 1` → no swap → `[4, 10, 3, 5, 1]`.
- `i = 0`: `a[0]=4` swaps with `a[1]=10` → `[10, 4, 3, 5, 1]`; recurse at `1` → `4` swaps with `a[3]=5` → **Max-Heap: `[10, 5, 3, 4, 1]`**.

### Phase 2 — Extract Maximum & Re-Heapify (`|` = locked sorted suffix)

| `i` | Swap `a[0] ↔ a[i]` | After `heapify(a, i, 0)` |
|---|---|---|
| `4` | `[1, 5, 3, 4 \| 10]` | `[5, 4, 3, 1 \| 10]` |
| `3` | `[1, 4, 3 \| 5, 10]` | `[4, 1, 3 \| 5, 10]` |
| `2` | `[3, 1 \| 4, 5, 10]` | `[3, 1 \| 4, 5, 10]` |
| `1` | `[1 \| 3, 4, 5, 10]` | **`[1, 3, 4, 5, 10]`** |

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet

| Operation / Case | Time Complexity | Space Complexity |
|---|---|---|
| **`heapify` (single call)** | **O(log n)** (tree height) | O(1) iterative / O(log n) recursive call stack |
| **Build Max-Heap (`n // 2` calls)** | **O(n)** (tight bound!) | — |
| **Heap Sort — Best / Average / Worst Time** | **O(n log n)** (all 3 cases!) | **O(1)** auxiliary array space (in-place) |

### Comparison: Heap Sort vs. Merge Sort vs. Quick Sort

| Parameter | Heap Sort | Merge Sort | Quick Sort |
|---|---|---|---|
| **Best-Case Time** | O(n log n) | O(n log n) | O(n log n) |
| **Average-Case Time** | O(n log n) | O(n log n) | O(n log n) |
| **Worst-Case Time** | **O(n log n)** | **O(n log n)** | **O(n²)** |
| **Extra Array Space** | **O(1) (in-place)** | **O(n)** | O(log n) stack |
| **Stable?** | **No** | **Yes** | **No** |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Passing `len(a)` instead of `i` in `heapify(a, i, 0)` during extraction:** Pulls already-sorted largest elements at the back of `a` right back to index `0`!
- **Mistake 2 — Using 1-based child formulas (`2*i`, `2*i + 1`) on a 0-based array:** Causes `2 * 0 = 0` self-comparison and infinite recursion.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define a Binary Heap and differentiate Max-Heap vs. Min-Heap. | A Binary Heap is a Complete Binary Tree stored in an array. In a **Max-Heap**, every parent `>=` its children (`a[0]` is max); in a **Min-Heap**, every parent `<=` its children (`a[0]` is min). |
| 2 | State the 0-based index formulas for parent, left child, and right child of index `i`. | Parent: **`(i - 1) // 2`**, Left child: **`2 * i + 1`**, Right child: **`2 * i + 2`**. |
| 3 | Why do we use a **Max-Heap** to sort in **ascending** order? | Because swapping the maximum at `a[0]` to the rightmost unsorted slot `a[i]` places largest elements at the end in place, leaving elements in ascending order. |
| 4 | State the best, average, and worst-case time complexities of Heap Sort. | **O(n log n)** in all three cases (Best, Average, and Worst). |
| 5 | State the time complexity of `heapify` vs. `build-heap` vs. full `heap_sort`. | `heapify`: **O(log n)**; `build-heap`: **O(n)**; full `heap_sort`: **O(n log n)**. |
| 6 | What is the auxiliary array space complexity of Heap Sort? | **O(1)** — it sorts **in place** without needing a separate auxiliary array. |
| 7 | Is Heap Sort stable? | **No**, Heap Sort is **unstable** because long-distance swaps between `a[0]` and `a[i]` can invert the relative order of equal elements. |
| 8 | Why does `build-heap` start from index `n // 2 - 1` down to `0`? | Indices `n // 2` through `n - 1` are **leaf nodes** (0 children), which already satisfy the heap property automatically. |
| 9 | Why is `i` passed as the second parameter `n` in `heapify(a, i, 0)` during Phase 2? | To restrict `heapify` to the unsorted heap prefix `0 .. i - 1` so already-sorted elements in `i .. len(a) - 1` remain untouched. |
| 10 | Compare Heap Sort and Merge Sort on space and stability. | Heap Sort is **in-place (`O(1)` extra array space)** and **unstable**; Merge Sort requires **`O(n)` extra space** and is **stable**. |
| 11 | Give three applications/uses of Binary Heaps. | (1) Heap Sort, (2) Priority Queues (OS scheduling, Dijkstra, Prim, A\*), and (3) finding top-`k` largest/smallest elements. |
| 12 | What is the height of a Binary Heap containing `n` elements? | **$\lfloor \log_2 n \rfloor$** (`O(log n)`). |
