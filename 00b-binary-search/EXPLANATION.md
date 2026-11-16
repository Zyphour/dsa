# Binary Search — Complete Reference & Code Guide (`binary_search.cpp`)

> **Aim:** Find a target value in a **sorted** array by repeatedly halving the search interval.
>
> **Language:** C++ · **Program:** [`binary_search.cpp`](binary_search.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`binary_search.cpp`](binary_search.cpp) asks the user for:
1. `n` — the number of elements (up to `10`),
2. `n` integers **already arranged in ascending sorted order**, stored in `arr[0 .. n - 1]`, and
3. `key` — the element to search for.

It initializes two index pointers `low = 0` and `high = n - 1`, repeatedly computes the middle index `mid = (low + high) / 2`, and compares `arr[mid]` with `key`:
- If `arr[mid] == key`, it prints `"Element found at position "` with `mid + 1` and terminates.
- If `arr[mid] < key`, it discards the left half (`low = mid + 1`).
- If `arr[mid] > key`, it discards the right half (`high = mid - 1`).
- If `low` crosses past `high` (`low > high`), the element is not in the array and it prints `"Element not found."`.

### Sample Run 1 (Element Found)
```text
Enter the number of elements: 5
Enter the sorted elements: 10 20 30 40 50
Enter the element to search: 40
Element found at position 4
```

### Sample Run 2 (Element Not Found)
```text
Enter the number of elements: 5
Enter the sorted elements: 10 20 30 40 50
Enter the element to search: 25
Element not found.
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Formula | Definition |
|---|---|
| **Binary Search (Half-Interval Search)** | A searching algorithm that finds a target key in a **sorted** array by comparing the key with the middle element and eliminating half of the remaining search range at every step. |
| **Divide and Conquer** | An algorithmic paradigm that breaks a problem into smaller subproblems; Binary Search reduces the active problem size from `n` to `n / 2` on every comparison (also called **Decrease and Conquer**). |
| **Sorted Array (Ascending)** | An array where every element is less than or equal to the next element: `arr[0] <= arr[1] <= ... <= arr[n - 1]`. |
| **`low` (Lower Bound)** | Starting index of the current active search subarray (initially `0`). |
| **`high` (Upper Bound)** | Ending index of the current active search subarray (initially `n - 1`). |
| **`mid` (Midpoint Index)** | Middle index of `[low, high]`, calculated as `(low + high) / 2` using integer division (fractional part truncated). |
| **Logarithmic Time `O(log n)`** | Growth rate proportional to $\log_2(n)$ — doubling `n` adds only **1** extra comparison! |

---

## 3. Core Facts, Rules, Advantages & Uses

### Mandatory Prerequisite & Key Rules
1. **Prerequisite:** The input array **MUST be sorted** beforehand. On unsorted data, discarding half the array based on `arr[mid]` produces wrong results.
2. **Loop Condition:** Must be **`while (low <= high)`** (NOT `low < high`), because when `low == high`, there is still **1 element** left at `arr[low]` to check.
3. **Bound Updates:** Must use **`low = mid + 1`** and **`high = mid - 1`** (never `low = mid` or `high = mid`, which can cause an infinite loop).
4. **Random Access Requirement:** Requires `O(1)` index lookup (`arr[mid]`), so it works efficiently on **arrays**, NOT on linked lists.

### Advantages & Disadvantages
- **Advantages:**
  1. Extremely fast on large sorted datasets: **O(log n)** worst-case time (`~10` checks for `1,000` items; `~20` checks for `1,000,000` items).
  2. Iterative version uses **O(1)** extra memory.
- **Disadvantages:**
  1. Cannot be used on **unsorted** arrays without sorting first (`O(n log n)`).
  2. Inefficient on **linked lists** because reaching the middle node takes `O(n)` pointer hops.

### Uses / Applications of Binary Search
1. Searching **sorted databases**, dictionaries, telephone directories, and student roll lists.
2. Database **B-Tree / index lookups** and standard library routines (`std::binary_search`, `std::lower_bound` in C++).
3. **Git bisect** — finding which commit in a chronological history introduced a bug.
4. Finding square roots, boundary thresholds, and optimization answers over monotonic ranges ("Binary Search on Answer").

---

## 4. Step-by-Step Algorithm

1. Start.
2. Read `n`, read `n` sorted integers into `arr[0 .. n - 1]`, and read `key`.
3. Set `low = 0` and `high = n - 1`.
4. Repeat while `low <= high`:
   - Calculate `mid = (low + high) / 2`.
   - If `arr[mid] == key`, print `"Element found at position "` + `(mid + 1)` and exit (`return 0`).
   - Else if `arr[mid] < key`, set `low = mid + 1` (search right half).
   - Else (`arr[mid] > key`), set `high = mid - 1` (search left half).
5. If `low > high`, print `"Element not found."`.
6. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int main() {
    int arr[10], n, key, low, high, mid;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the sorted elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "Enter the element to search: "; cin >> key;
    low = 0; high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (arr[mid] == key) { cout << "Element found at position " << mid + 1; return 0; }
        else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    cout << "Element not found.";
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `int arr[10], n, key, low, high, mid;` | Declares static array `arr` (capacity 10), active element count `n`, target `key`, and index variables `low`, `high`, `mid`. |
| `cin >> n;` | Reads how many elements (`1..10`) will be stored. |
| `for (int i = 0; i < n; i++) cin >> arr[i];` | Reads `n` ascending-sorted integers into `arr[0 .. n - 1]`. |
| `cin >> key;` | Reads the search target. |
| `low = 0; high = n - 1;` | Sets initial search range to cover the entire array. |
| `while (low <= high)` | Continues searching as long as the range `[low .. high]` contains at least 1 element. |
| `mid = (low + high) / 2;` | Computes the middle index via integer division (e.g., `(0 + 5) / 2 = 2`). |
| `if (arr[mid] == key) { ... return 0; }` | If the middle value equals `key`, prints 1-based position `mid + 1` and terminates `main()`. |
| `else if (arr[mid] < key) low = mid + 1;` | Target is larger than `arr[mid]`, so `arr[low .. mid]` is eliminated; search continues in `mid + 1 .. high`. |
| `else high = mid - 1;` | Target is smaller than `arr[mid]`, so `arr[mid .. high]` is eliminated; search continues in `low .. mid - 1`. |
| `cout << "Element not found.";` | Executes only if the `while` loop ends (`low > high`), meaning `key` does not exist in `arr`. |

---

## 6. Step-by-Step Dry Runs

### Dry Run 1 — Target Found (`n = 5`, `arr = [10, 20, 30, 40, 50]`, `key = 40`)

| Step | `low` | `high` | `mid = (low+high)/2` | `arr[mid]` | Comparison | Update / Result |
|---|---|---|---|---|---|---|
| 1 | `0` | `4` | `(0 + 4) / 2 = 2` | `30` | `30 < 40` | `low = 2 + 1 = 3` |
| 2 | `3` | `4` | `(3 + 4) / 2 = 3` | `40` | `40 == 40` | Print `Element found at position 4`, exit |

### Dry Run 2 — Target Not Found (`n = 5`, `arr = [10, 20, 30, 40, 50]`, `key = 25`)

| Step | `low` | `high` | `low <= high`? | `mid` | `arr[mid]` | Comparison | Update / Result |
|---|---|---|---|---|---|---|---|
| 1 | `0` | `4` | True | `2` | `30` | `30 > 25` | `high = 2 - 1 = 1` |
| 2 | `0` | `1` | True | `0` | `10` | `10 < 25` | `low = 0 + 1 = 1` |
| 3 | `1` | `1` | True | `1` | `20` | `20 < 25` | `low = 1 + 1 = 2` |
| 4 | `2` | `1` | **False** | — | — | Loop ends | Print `Element not found.` |

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet (for `n` sorted elements)

| Metric | Complexity | Exact Condition / Reason |
|---|---|---|
| **Best-Case Time Complexity** | **O(1)** | `key` matches the initial middle element `arr[(n - 1) / 2]` on Step 1. |
| **Average-Case Time Complexity** | **O(log n)** | Search space halves every step ($\log_2 n$). |
| **Worst-Case Time Complexity** | **O(log n)** | `key` is found at the final 1-element range or is absent ($\lfloor \log_2 n \rfloor + 1$ comparisons). |
| **Auxiliary Space (Iterative — this code)** | **O(1)** | Uses only scalar integer variables (`low`, `high`, `mid`, `key`, `n`). |
| **Auxiliary Space (Recursive version)** | **O(log n)** | Recursion call stack stores up to $\log_2 n$ frames. |

*(Formula note: After $k$ halvings, remaining size is $n / 2^k = 1 \implies 2^k = n \implies k = \log_2 n$. Overflow-safe midpoint formula for huge arrays: `mid = low + (high - low) / 2`.)*

### Comparison: Linear Search vs. Binary Search

| Parameter | Linear Search | Binary Search |
|---|---|---|
| **Input Order** | Any (sorted or unsorted) | **Sorted only** |
| **Best / Worst Time** | O(1) / **O(n)** | O(1) / **O(log n)** |
| **Worst-Case Steps for `n = 1,000`** | `1,000` | `~10` (`⌊log₂ 1000⌋ + 1 = 10`) |
| **Worst-Case Steps for `n = 1,024`** | `1,024` | `11` (`log₂ 1024 + 1 = 11`) |
| **Extra Space (Iterative)** | O(1) | O(1) |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Unsorted Input:** Entering unsorted numbers violates Binary Search's core assumption and returns wrong answers.
- **Mistake 2 — Writing `low < high` instead of `low <= high`:** Skips checking the final candidate when `low == high`.
- **Mistake 3 — Writing `low = mid` or `high = mid`:** Fails to shrink a 2-element range and causes an infinite loop.
- **Mistake 4 — Comparing `mid == key` instead of `arr[mid] == key`:** Compares the array *index* instead of the array *element*.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define Binary Search. | Binary Search is a Divide-and-Conquer searching algorithm that locates a target value in a **sorted** array by repeatedly comparing the target with the middle element and halving the search interval. |
| 2 | What is the essential precondition/prerequisite for Binary Search? | The array **must be sorted** (in ascending or descending order) prior to searching. |
| 3 | State the best, average, and worst-case time complexities of Binary Search. | Best case: **O(1)**, Average case: **O(log n)**, Worst case: **O(log n)**. |
| 4 | What is the space complexity of iterative vs. recursive Binary Search? | Iterative Binary Search: **O(1)** auxiliary space. Recursive Binary Search: **O(log n)** auxiliary call-stack space. |
| 5 | Which algorithmic design technique does Binary Search use? | **Divide and Conquer** (specifically Decrease and Conquer). |
| 6 | Why is Binary Search's worst-case time complexity `O(log n)`? | Because every comparison divides the active search range by `2` (`n → n/2 → n/4 → ... → 1`), taking at most $\lfloor \log_2 n \rfloor + 1$ steps. |
| 7 | Maximum comparisons needed by Binary Search for `1,024` elements? | `log₂(1024) + 1 = 10 + 1 =` **11 comparisons**. |
| 8 | Why must the `while` condition be `low <= high` and not `low < high`? | When `low == high`, the search interval still contains 1 unchecked element (`arr[low]`). |
| 9 | Why is Binary Search not suitable for linked lists? | Linked lists do not support `O(1)` random access (`arr[mid]`); finding the middle node takes `O(n)` traversal. |
| 10 | How do you avoid integer overflow when computing `mid` for very large indices? | Write `mid = low + (high - low) / 2;` instead of `(low + high) / 2;`. |
| 11 | Give three applications/uses of Binary Search. | (1) Searching sorted databases/dictionaries, (2) C++ STL `binary_search` / `lower_bound`, and (3) `git bisect` debugging. |
| 12 | What condition signals that the target element is NOT present in the array? | `low > high` (`low` crosses past `high`, leaving an empty search interval). |
