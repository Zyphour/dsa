# Linear Search — Complete Reference & Code Guide (`linear_search.cpp`)

> **Aim:** Search for a target value in an array by checking each element from start to end.
>
> **Language:** C++ · **Program:** [`linear_search.cpp`](linear_search.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`linear_search.cpp`](linear_search.cpp) takes **5 integers** from the user, stores them in an array `a[5]`, and asks for a **target number (`key`)** to find. It then scans the array from index `0` to index `4`:
- **If `key` is present:** It prints the **1-based position** (`index + 1`) of the **first match** and stops immediately.
- **If `key` is absent:** After checking all 5 elements, it prints `"Not Found"`.

### Sample Run 1 (Element Found)
```text
Enter 5 elements: 10 30 20 50 40
Enter value to search: 20
Found at position 3
```

### Sample Run 2 (Element Not Found)
```text
Enter 5 elements: 10 30 20 50 40
Enter value to search: 99
Not Found
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Definition |
|---|---|
| **Searching** | The process of finding the location (index or position) of a given target element inside a data collection. |
| **Linear Search (Sequential Search)** | A searching algorithm that checks every element of a list one by one sequentially from the beginning until the target element is found or the list ends. |
| **Array** | A linear data structure that stores a fixed-size collection of elements of the **same data type** in **contiguous (adjacent) memory locations**. |
| **Key (Target)** | The specific value being searched for inside the data structure. |
| **0-Based Indexing** | Numbering array slots starting from `0` (`a[0], a[1], ..., a[n - 1]`). Used in C, C++, Python, and Java. |
| **1-Based Position** | Human counting position starting from `1` (`position = index + 1`). |
| **DSA** | **Full Form:** *Data Structures and Algorithms*. |
| **I/O** | **Full Form:** *Input / Output* (handled in C++ by `<iostream>`: `cin` for input, `cout` for output). |

---

## 3. Core Facts, Properties, Advantages & Uses

### Key Properties
- **Sorting Prerequisite:** **None.** Works on **both sorted and unsorted** arrays.
- **Algorithmic Approach:** Brute-force / Sequential traversal.
- **Duplicate Handling:** Always returns the **first (leftmost)** occurrence because traversal goes left to right (`0 → n - 1`) and exits on the first match.
- **Data Structure Compatibility:** Works on both **arrays** and **linked lists** (only sequential access is required, not random access).

### Advantages & Disadvantages
- **Advantages:**
  1. Simple to understand and implement.
  2. Requires **no sorting** or preprocessing beforehand.
  3. Requires **O(1)** extra memory.
- **Disadvantages:**
  1. Slow on large datasets (**O(n)** time — checking 1,000,000 items can take 1,000,000 comparisons).
  2. Inefficient when repeated searches are performed on static data (where sorting once + Binary Search is much faster).

### Uses / Applications of Linear Search
1. Searching **unsorted** arrays or lists.
2. Searching **small datasets** (e.g., fewer than 20–50 elements) where overhead of sorting is unnecessary.
3. Searching **singly or doubly linked lists**, where direct middle-element indexing (`O(1)`) is impossible.
4. Performing a **one-time search** on unsorted data (sorting costs `O(n log n)`, which is slower than a single `O(n)` scan).

---

## 4. Step-by-Step Algorithm

1. Start.
2. Declare integer array `a[5]` and integer `key`.
3. Read 5 elements into `a[0]` through `a[4]`.
4. Read the target value `key`.
5. Loop `i` from `0` to `4`:
   - If `a[i] == key`, print `"Found at position "` followed by `i + 1` and **exit** (`return 0`).
6. If the loop finishes without finding `key`, print `"Not Found"`.
7. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int main() {
    int a[5], key;
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) cin >> a[i];
    cout << "Enter value to search: "; cin >> key;
    for (int i = 0; i < 5; i++) {
        if (a[i] == key) { cout << "Found at position " << i + 1; return 0; }
    }
    cout << "Not Found";
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `#include <iostream>` | Preprocessor directive that includes the standard input-output stream header (`cin`, `cout`). |
| `using namespace std;` | Allows direct use of standard library names (`cin`, `cout`) without writing `std::`. |
| `int main()` | Main entry function where program execution starts. Returns `int` exit status (`0` = success). |
| `int a[5], key;` | Allocates a 5-integer array `a` (`indices 0..4`) and an integer `key` to store the search target. |
| `for (int i = 0; i < 5; i++) cin >> a[i];` | Loops `i = 0, 1, 2, 3, 4` and reads 5 user-entered integers into `a[0]..a[4]`. |
| `cin >> key;` | Reads the integer to search for into `key`. |
| `for (int i = 0; i < 5; i++)` | Loops sequentially over every valid index `0..4` of `a`. |
| `if (a[i] == key)` | Equality comparison (`==`) checking whether current element `a[i]` matches `key`. |
| `cout << "Found at position " << i + 1;` | Prints the 1-based position (`index + 1`). |
| `return 0;` *(inside `if`)* | Terminates `main()` immediately as soon as `key` is found so `"Not Found"` is NOT printed afterward. |
| `cout << "Not Found";` | Reached **only** if all 5 loop iterations completed without matching `key`. |
| `return 0;` *(at end)* | Ends `main()` normally after printing `"Not Found"`. |

---

## 6. Step-by-Step Dry Run

**Input:** `a = [10, 30, 20, 50, 40]`, `key = 20`

| Step | `i` | `i < 5`? | `a[i]` | `a[i] == 20`? | Action |
|---|---|---|---|---|---|
| 1 | `0` | True | `10` | False (`10 != 20`) | Increment `i` to `1` |
| 2 | `1` | True | `30` | False (`30 != 20`) | Increment `i` to `2` |
| 3 | `2` | True | `20` | **True (`20 == 20`)** | Print `Found at position 3`, execute `return 0` (stop) |

---

## 7. Time & Space Complexity + Comparison

### Complexity Fact Sheet (for an array of `n` elements)

| Metric | Complexity | Exact Condition / Reason |
|---|---|---|
| **Best-Case Time Complexity** | **O(1)** | Target `key` is found at the first index `a[0]` (1 comparison). |
| **Average-Case Time Complexity** | **O(n)** | Target is near the middle (`(n + 1) / 2` comparisons on average). |
| **Worst-Case Time Complexity** | **O(n)** | Target is at the last index `a[n - 1]` **or** is not in the array (`n` comparisons). |
| **Auxiliary Space Complexity** | **O(1)** | Uses only constant extra variables (`i`, `key`), independent of `n`. |
| **Total Space Complexity** | **O(n)** | `n` slots to store the input array itself. |

### Comparison: Linear Search vs. Binary Search

| Parameter | Linear Search | Binary Search |
|---|---|---|
| **Input Order Requirement** | None (works on sorted & unsorted data) | **Must be sorted** |
| **Technique** | Sequential scan | Divide and Conquer |
| **Best-Case Time** | O(1) | O(1) |
| **Average-Case Time** | O(n) | O(log n) |
| **Worst-Case Time** | **O(n)** | **O(log n)** |
| **Auxiliary Space (Iterative)** | O(1) | O(1) |
| **Best Used For** | Small or unsorted arrays; linked lists | Large sorted arrays |

---

## 8. Important Exam Points & Common Mistakes

- **Exam Fact 1:** Linear Search returns the **first** occurrence when duplicate values exist.
- **Exam Fact 2:** `i + 1` converts 0-based C++ array index (`0..4`) into 1-based position (`1..5`).
- **Mistake 1 — Using `break;` instead of `return 0;` without a flag:** `break;` only exits the `for` loop and still executes `cout << "Not Found";` right below it.
- **Mistake 2 — Writing `i <= 5` instead of `i < 5`:** Accesses `a[5]`, which is out of array bounds (valid indices are `0..4`).
- **Mistake 3 — Writing `=` instead of `==` in `if (a[i] == key)`:** `=` assigns `key` to `a[i]` instead of comparing them.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define Linear Search. | Linear Search (or Sequential Search) is an algorithm that searches for a key by checking each element sequentially from index `0` to `n - 1` until a match is found or the array ends. |
| 2 | What is another name for Linear Search? | **Sequential Search**. |
| 3 | Does Linear Search require the array to be sorted? | **No**, it works on both sorted and unsorted arrays. |
| 4 | State the best-case, average-case, and worst-case time complexities of Linear Search. | Best case: **O(1)**, Average case: **O(n)**, Worst case: **O(n)**. |
| 5 | When do the best case and worst case occur in Linear Search? | **Best case:** target is at index `0`. **Worst case:** target is at the last index `n - 1` or is absent from the array. |
| 6 | What is the auxiliary space complexity of Linear Search? | **O(1)** (constant extra space). |
| 7 | How many comparisons does Linear Search take in the worst case for `n = 500` elements? | **500 comparisons**. |
| 8 | What happens if the target key occurs twice in the array? | It reports the position of the **first occurrence** and stops immediately. |
| 9 | Why do we print `i + 1` instead of `i`? | Because C++ array indices start at `0`, while human-readable positions start at `1`. |
| 10 | Give three applications/uses of Linear Search. | (1) Searching unsorted arrays, (2) searching small lists, and (3) searching linked lists. |
| 11 | Define an Array. | An array is a collection of elements of the same data type stored in contiguous memory locations and accessed by numerical index. |
| 12 | Why is `return 0;` placed inside the `if` statement? | To exit `main()` immediately after finding the element so `"Not Found"` does not get printed. |
