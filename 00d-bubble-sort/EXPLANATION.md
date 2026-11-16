# Bubble Sort — Complete Reference & Code Guide (`bubble_sort.cpp`)

> **Aim:** Sort an array of integers in ascending order using Bubble Sort.
>
> **Language:** C++ · **Program:** [`bubble_sort.cpp`](bubble_sort.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`bubble_sort.cpp`](bubble_sort.cpp) reads an array size `n` (up to `100`) and `n` unsorted integers into `a[0 .. n - 1]`. It sorts the array **in place in ascending order** (smallest to largest) by running `n - 1` passes over the array, comparing every adjacent pair `(a[j], a[j + 1])`, and swapping them whenever `a[j] > a[j + 1]`. Finally, it prints the sorted array.

### Sample Run
```text
Enter size: 5
Enter elements: 64 34 25 12 22
Sorted array: 12 22 25 34 64 
```

---

## 2. Definitions & Key Terminology

| Term | Definition |
|---|---|
| **Sorting** | Arranging elements of a list in a specific monotonic order — **ascending** (smallest to largest) or **descending** (largest to smallest). |
| **Bubble Sort (Sinking Sort)** | A comparison-based sorting algorithm that repeatedly steps through the array, compares **adjacent elements**, and swaps them if they are in the wrong order, moving the largest unsorted element to its final position at the end of each pass. |
| **Pass** | One complete scan of the inner loop across the unsorted portion of the array. An array of `n` elements requires at most **`n - 1` passes**. |
| **Swap** | Exchanging the values stored in two memory locations using a temporary variable (`temp = x; x = y; y = temp;`). |
| **In-Place Sorting** | Sorting directly inside the original array using only **O(1)** constant extra memory (no auxiliary array copy). |
| **Stable Sorting Algorithm** | A sorting algorithm that **preserves the original relative order of equal elements** (if two items have equal keys, whichever appeared first in the input still appears first in the output). |
| **Internal vs. External Sorting** | **Internal sorting** sorts data entirely inside main memory (RAM), like Bubble Sort; **external sorting** sorts massive datasets stored on disk. |

---

## 3. Core Facts, Properties, Advantages & Uses

### Key Properties of Bubble Sort
- **Method:** Comparison-based, Exchange / Adjacent-swap sort.
- **In-Place?** **Yes** (`O(1)` auxiliary space — only `temp`, `i`, `j`).
- **Stable?** **Yes** — swaps happen strictly when `a[j] > a[j + 1]`, never on equality (`==`), so equal values never cross over one another.
- **Pass Guarantee:** After pass `k` (`1st, 2nd, ...`), the **`k` largest elements** are permanently placed in the **last `k` indices** of the array.
- **Maximum Comparisons & Swaps:** $\frac{n(n - 1)}{2}$ comparisons; up to $\frac{n(n - 1)}{2}$ swaps (when input is reverse-sorted).

### Advantages & Disadvantages
- **Advantages:**
  1. Very short and simple code (`3` lines of sorting logic).
  2. **In-place (`O(1)` extra space)** and **stable**.
  3. With a `bool swapped` flag, it can detect an already-sorted array in **O(n)** time.
- **Disadvantages:**
  1. **O(n²)** time complexity makes it very slow on large datasets (`n > 1,000`).
  2. Performs **O(n²) swaps** (3 writes per swap), making it slower in practice than both Selection Sort and Insertion Sort.

### Uses / Applications of Bubble Sort
1. Teaching foundational sorting concepts, nested loops, and loop invariants.
2. Sorting **very small arrays** where code simplicity matters more than speed.
3. **Sortedness check / nearly-sorted data** (when using the early-exit `swapped` flag, 1 pass verifies an array is sorted in `O(n)`).

---

## 4. Step-by-Step Algorithm

1. Start.
2. Read size `n` and read `n` integers into `a[0 .. n - 1]`.
3. **Outer loop (passes):** For `i = 0` to `n - 2` (`n - 1` passes):
   - **Inner loop (adjacent comparisons):** For `j = 0` to `n - i - 2`:
     - If `a[j] > a[j + 1]`, swap `a[j]` and `a[j + 1]`:
       `temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp;`
4. Print all `n` elements of `a[0 .. n - 1]`.
5. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int main() {
    int a[100], n, temp;
    cout << "Enter size: "; cin >> n;
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (a[j] > a[j + 1]) { temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp; }
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `int a[100], n, temp;` | Allocates capacity for up to `100` integers, `n` for actual element count, and `temp` for swapping. |
| `for (int i = 0; i < n; i++) cin >> a[i];` | Reads `n` integers into `a[0 .. n - 1]`. |
| `for (int i = 0; i < n - 1; i++)` | Outer loop running **`n - 1` passes** (`0` to `n - 2`). Once `n - 1` largest items are placed, the remaining 1st item is automatically sorted. |
| `for (int j = 0; j < n - i - 1; j++)` | Inner loop scanning unsorted adjacent pairs. `- 1` keeps `a[j + 1]` in bounds (`<= n - 1`); `- i` skips the last `i` elements already locked in sorted order. |
| `if (a[j] > a[j + 1])` | Tests whether the left element is strictly greater than the right element (out of ascending order). |
| `{ temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp; }` | Standard 3-statement swap exchanging `a[j]` and `a[j + 1]`. |
| `for (int i = 0; i < n; i++) cout << a[i] << " ";` | Prints the sorted elements separated by spaces. |

---

## 6. Step-by-Step Dry Run

**Input:** `n = 4`, `a = [5, 1, 4, 2]`

| Pass `i` | `j` | Pair `(a[j], a[j+1])` | `a[j] > a[j+1]`? | Swap? | Array State (`\|` = sorted suffix) |
|---|---|---|---|---|---|
| `i = 0` | `0` | `(5, 1)` | True | Yes | `[1, 5, 4, 2]` |
| `i = 0` | `1` | `(5, 4)` | True | Yes | `[1, 4, 5, 2]` |
| `i = 0` | `2` | `(5, 2)` | True | Yes | `[1, 4, 2 \| 5]` |
| `i = 1` | `0` | `(1, 4)` | False | No | `[1, 4, 2 \| 5]` |
| `i = 1` | `1` | `(4, 2)` | True | Yes | `[1, 2 \| 4, 5]` |
| `i = 2` | `0` | `(1, 2)` | False | No | `[1 \| 2, 4, 5]` |

**Final Output:** `Sorted array: 1 2 4 5 `

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet

- **Exact Comparisons:** $(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2} = O(n^2)$.

| Metric | Standard Bubble Sort (this code) | Optimized Bubble Sort (with `swapped` flag) |
|---|---|---|
| **Best-Case Time** (already sorted) | **O(n²)** (`n(n-1)/2` comparisons, `0` swaps) | **O(n)** (`n - 1` comparisons, exits after Pass 1) |
| **Average-Case Time** (random order) | **O(n²)** | **O(n²)** |
| **Worst-Case Time** (reverse sorted) | **O(n²)** (`n(n-1)/2` comparisons & swaps) | **O(n²)** |
| **Auxiliary Space Complexity** | **O(1)** (in-place) | **O(1)** (in-place) |
| **Stable?** | **Yes** | **Yes** |

### Comparison: Bubble Sort vs. Selection Sort vs. Insertion Sort

| Parameter | Bubble Sort | Selection Sort | Insertion Sort |
|---|---|---|---|
| **Best-Case Time** | O(n²) *(O(n) with flag)* | O(n²) | **O(n)** |
| **Average / Worst Time** | O(n²) / O(n²) | O(n²) / O(n²) | O(n²) / O(n²) |
| **Worst-Case Swaps / Writes** | **O(n²)** swaps | **O(n)** swaps (`<= n - 1`) | O(n²) shifts |
| **Auxiliary Space** | O(1) | O(1) | O(1) |
| **Stable?** | **Yes** | **No** | **Yes** |

---

## 8. Important Exam Points & Common Mistakes

- **Descending Order Modification:** Change `>` to `<` (`if (a[j] < a[j + 1])`).
- **Optimized Early-Exit Modification:** Set `bool swapped = false;` before the `j` loop, set `swapped = true;` inside the `if`, and write `if (!swapped) break;` after the `j` loop.
- **Mistake 1 — Writing `j < n` instead of `j < n - i - 1`:** Causes `a[j + 1]` to access `a[n]` out of bounds.
- **Mistake 2 — Using `>=` instead of `>`:** Breaks stability by swapping equal elements unnecessarily.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define Bubble Sort. | Bubble Sort is an in-place comparison sorting algorithm that repeatedly compares adjacent elements and swaps them if out of order, moving the largest remaining element to the end on each pass. |
| 2 | State the best, average, and worst-case time complexities of Bubble Sort. | Standard Bubble Sort: **O(n²)** in best, average, and worst cases. With an early-exit `swapped` flag: **O(n)** best case, **O(n²)** average and worst cases. |
| 3 | What is the auxiliary space complexity of Bubble Sort? | **O(1)** (constant extra memory; it is an in-place algorithm). |
| 4 | Is Bubble Sort a stable sorting algorithm? Why? | **Yes**, because it swaps strictly when `a[j] > a[j + 1]` and never swaps equal elements (`a[j] == a[j + 1]`). |
| 5 | What is an in-place sorting algorithm? | An algorithm that sorts data inside the original input array using only `O(1)` constant auxiliary memory. |
| 6 | Maximum number of passes required by Bubble Sort for `n` elements? | **`n - 1` passes**. |
| 7 | Exact formula for total comparisons in unoptimized Bubble Sort? | **`n(n - 1) / 2`** comparisons. |
| 8 | Why does the inner loop terminate at `n - i - 1`? | `- 1` prevents `a[j + 1]` from going out of bounds, and `- i` skips the last `i` elements that are already sorted after `i` passes. |
| 9 | Which input triggers the worst case of Bubble Sort? | An array sorted in **reverse (descending) order**, forcing a swap on every single comparison. |
| 10 | How do you convert this ascending Bubble Sort into descending order? | Replace `if (a[j] > a[j + 1])` with `if (a[j] < a[j + 1])`. |
| 11 | What is another name for Bubble Sort? | **Sinking Sort** (or Exchange Sort). |
| 12 | Give two uses of Bubble Sort. | (1) Sorting tiny arrays with minimal code, and (2) checking in `O(n)` whether a list is already sorted (with the `swapped` flag). |
