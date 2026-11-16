# Selection Sort — Complete Reference & Code Guide (`selection_sort.cpp`)

> **Aim:** Sort an array of integers in ascending order using Selection Sort.
>
> **Language:** C++ · **Program:** [`selection_sort.cpp`](selection_sort.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`selection_sort.cpp`](selection_sort.cpp) reads an integer `n` (up to `100`) and `n` unsorted integers into `arr[0 .. n - 1]`. It sorts the array **in place in ascending order** by dividing the array into a **sorted left prefix** and an **unsorted right suffix**. On each pass `i` (`0` to `n - 2`), it scans the unsorted suffix `i .. n - 1` to find the **index `min` of the smallest remaining element**, performs **one swap** between `arr[i]` and `arr[min]`, and finally prints the sorted array.

### Sample Run
```text
Enter the number of elements: 4
Enter the elements: 64 25 12 22
Sorted array: 12 22 25 64 
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Definition |
|---|---|
| **Selection Sort** | An in-place comparison-based sorting algorithm that repeatedly finds the minimum element from the unsorted subarray and swaps it into the first position of that unsorted subarray. |
| **Sorted Prefix (`0 .. i - 1`)** | The left portion of the array that already holds the `i` globally smallest elements in final ascending order. |
| **Unsorted Suffix (`i .. n - 1`)** | The remaining right portion of the array yet to be sorted. |
| **`min` (Minimum Index)** | Integer variable holding the **array index** (NOT the value) of the smallest element found so far during the current pass. |
| **Unstable Sort** | A sorting algorithm that **can change the relative order of equal elements** (e.g., in `[4a, 4b, 1]`, swapping `4a` with `1` gives `[1, 4b, 4a]`). |
| **EEPROM / Flash** | **Full Form:** *Electrically Erasable Programmable Read-Only Memory* — hardware memory where write operations are slow/limited, making Selection Sort's minimal `O(n)` swaps advantageous. |

---

## 3. Core Facts, Properties, Advantages & Uses

### Key Properties of Selection Sort
- **Method:** Comparison-based, Selection & Swap sort.
- **In-Place?** **Yes** — uses **O(1)** extra memory (`min`, `temp`, `i`, `j`).
- **Stable?** **No** — long-distance swaps (`arr[i] ↔ arr[min]`) can jump an item over an equal key.
- **Total Comparisons:** Always $\frac{n(n - 1)}{2} = O(n^2)$ in **every** case (even if already sorted).
- **Total Swaps:** At most **`n - 1` swaps (`O(n)`)** — the minimum number of swaps among elementary sorting algorithms.

### Advantages & Disadvantages
- **Advantages:**
  1. Performs **at most `n - 1` swaps (`O(n)` memory writes)**, far fewer than Bubble Sort's `O(n²)` swaps.
  2. **In-place (`O(1)` auxiliary space)** and simple to implement.
- **Disadvantages:**
  1. **O(n²)** comparisons in **all cases** (Best, Average, and Worst) — cannot finish early on already-sorted input.
  2. **Not stable** in its standard swap-based array form.

### Uses / Applications of Selection Sort
1. Systems where **memory writes / swaps are much more expensive than reads/comparisons** (e.g., Flash memory, EEPROM, or swapping very large records).
2. Sorting **small lists** (`n <= 20–30`).
3. Finding the **top `k` smallest (or largest) elements** without sorting the whole array — stopping after `k` passes gives the `k` smallest elements in `O(n · k)` time.

---

## 4. Step-by-Step Algorithm

1. Start.
2. Read `n` and read `n` integers into `arr[0 .. n - 1]`.
3. **Outer loop:** For `i = 0` to `n - 2`:
   - Set `min = i`.
   - **Inner loop:** For `j = i + 1` to `n - 1`:
     - If `arr[j] < arr[min]`, update `min = j`.
   - Swap `arr[i]` and `arr[min]` using `temp`:
     `temp = arr[i]; arr[i] = arr[min]; arr[min] = temp;`
4. Print `arr[0 .. n - 1]`.
5. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int main() {
    int arr[100], n, temp;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++) cin >> arr[i];
    for(int i = 0; i < n - 1; i++) {
        int min = i;
        for(int j = i + 1; j < n; j++)
            if(arr[j] < arr[min]) min = j;
        temp = arr[i]; arr[i] = arr[min]; arr[min] = temp;
    }
    cout << "Sorted array: ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `int arr[100], n, temp;` | Declares array `arr` (max size 100), element count `n`, and swap variable `temp`. |
| `for(int i = 0; i < n; i++) cin >> arr[i];` | Reads `n` integers from standard input into `arr[0 .. n - 1]`. |
| `for(int i = 0; i < n - 1; i++)` | Outer loop selecting target slot `i` (`0` to `n - 2`). Last element at `n - 1` falls into place automatically. |
| `int min = i;` | Initializes `min` to index `i` (assuming `arr[i]` is the minimum of `i .. n - 1`). |
| `for(int j = i + 1; j < n; j++)` | Scans every remaining element after `i` up to index `n - 1`. |
| `if(arr[j] < arr[min]) min = j;` | Whenever a smaller element is found, records its **index** `j` in `min`. |
| `temp = arr[i]; arr[i] = arr[min]; arr[min] = temp;` | Executes **once per pass** (outside the `j` loop) to swap the smallest element of `i .. n - 1` into `arr[i]`. |
| `for(int i = 0; i < n; i++) cout << arr[i] << " ";` | Prints the sorted array. |

---

## 6. Step-by-Step Dry Run

**Input:** `n = 4`, `arr = [64, 25, 12, 22]`

| Pass `i` | Initial `min` | Inner Scan `j` (`i+1 .. 3`) | Final `min` (`arr[min]`) | Swap `arr[i] ↔ arr[min]` | Array After Pass (`\|` = sorted prefix) |
|---|---|---|---|---|---|
| `0` | `0` (`64`) | `j=1`: `25<64 → min=1`<br>`j=2`: `12<25 → min=2`<br>`j=3`: `22<12` (False) | `2` (`12`) | `arr[0] ↔ arr[2]` | `[12 \| 25, 64, 22]` |
| `1` | `1` (`25`) | `j=2`: `64<25` (False)<br>`j=3`: `22<25 → min=3` | `3` (`22`) | `arr[1] ↔ arr[3]` | `[12, 22 \| 64, 25]` |
| `2` | `2` (`64`) | `j=3`: `25<64 → min=3` | `3` (`25`) | `arr[2] ↔ arr[3]` | `[12, 22, 25 \| 64]` |

**Final Output:** `Sorted array: 12 22 25 64 `

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet

| Metric | Complexity | Exact Reason |
|---|---|---|
| **Best-Case Time Complexity** | **O(n²)** | Always performs `n(n - 1) / 2` comparisons even on an already-sorted array. |
| **Average-Case Time Complexity** | **O(n²)** | `n(n - 1) / 2` comparisons. |
| **Worst-Case Time Complexity** | **O(n²)** | `n(n - 1) / 2` comparisons. |
| **Number of Swaps (All Cases)** | **O(n)** | At most **`n - 1` swaps** (1 swap per pass). |
| **Auxiliary Space Complexity** | **O(1)** | In-place; uses only scalar variables (`min`, `temp`, `i`, `j`). |
| **Stable?** | **No** | Unstable due to non-adjacent swaps. |

### Comparison: Selection Sort vs. Bubble Sort

| Parameter | Selection Sort | Bubble Sort |
|---|---|---|
| **Core Mechanism** | Find minimum index, 1 swap per pass | Swap adjacent out-of-order pairs |
| **Comparisons (Best / Worst)** | **O(n²) / O(n²)** | O(n)\* / O(n²) |
| **Swaps (Worst Case)** | **At most `n - 1` (`O(n)`)** | Up to `n(n - 1) / 2` (`O(n²)`) |
| **Auxiliary Space** | O(1) | O(1) |
| **Stable?** | **No** | **Yes** |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Storing value `min = arr[i]` instead of index `min = i`:** Breaks `arr[min]` during comparison and swapping.
- **Mistake 2 — Placing the swap *inside* the inner `j` loop:** Causes multiple unnecessary swaps per pass instead of 1 swap at the end.
- **Mistake 3 — Starting `j = 0` instead of `j = i + 1`:** Corrupts the already-sorted left prefix `0 .. i - 1`.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define Selection Sort. | Selection Sort is an in-place comparison sort that repeatedly selects the minimum element from the unsorted subarray `i .. n - 1` and swaps it with `arr[i]`. |
| 2 | State the best, average, and worst-case time complexities of Selection Sort. | **O(n²)** in all three cases (Best, Average, and Worst). |
| 3 | Why is Selection Sort's best-case time complexity still `O(n²)`? | Because even if the array is already sorted, the inner loop must still scan all remaining elements on every pass to verify the minimum. |
| 4 | What is the space complexity of Selection Sort? | **O(1)** auxiliary space (in-place). |
| 5 | What is the maximum number of swaps performed by Selection Sort for `n` elements? | **`n - 1` swaps** (`O(n)`). |
| 6 | Is Selection Sort stable? | **No**, standard Selection Sort is **unstable** because swapping non-adjacent elements can invert the order of duplicate values. |
| 7 | What is Selection Sort's main advantage over Bubble Sort? | It performs at most **`n - 1` swaps (`O(n)`)** instead of up to `n(n - 1)/2` (`O(n²)`) swaps, minimizing memory writes. |
| 8 | What does the variable `min` store in `selection_sort.cpp`? | The **index** of the smallest element found so far in the unsorted suffix `i .. n - 1`. |
| 9 | Why does the outer loop run only up to `n - 2` (`i < n - 1`)? | Once the `n - 1` smallest elements are placed at indices `0 .. n - 2`, the final element at `n - 1` is automatically the largest. |
| 10 | Give two applications/uses of Selection Sort. | (1) Sorting small arrays when memory write operations are costly (e.g., EEPROM/Flash), and (2) finding the `k` smallest elements in `k` passes. |
| 11 | How do you modify Selection Sort to sort in descending order? | Track `max = i` and flip `<` to `>`: `if (arr[j] > arr[max]) max = j;`. |
| 12 | Which `O(n log n)` sorting algorithm improves upon Selection Sort using a tree data structure? | **Heap Sort** (replaces the `O(n)` linear minimum/maximum scan with an `O(log n)` heap operation). |
