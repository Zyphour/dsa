# Linear & Binary Search (Menu) — Complete Reference & Code Guide (`linear_binary_search.cpp`)

> **Aim:** Provide a menu-driven C++ program to search an array using either Linear Search or Binary Search.
>
> **Language:** C++ · **Program:** [`linear_binary_search.cpp`](linear_binary_search.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`linear_binary_search.cpp`](linear_binary_search.cpp) lets the user enter an array of `n` integers (up to `10`), displays a **2-option menu**, asks for `choice` (`1` or `2`) and the search target `key`, and uses a C++ `switch` statement to run the chosen search:
- **Choice `1` (Linear Search):** Scans `arr[0 .. n - 1]` left-to-right (works on sorted or unsorted input).
- **Choice `2` (Binary Search):** Halves `[low .. high]` repeatedly (requires the entered elements to be **sorted in ascending order**).
- **Any other choice (`default`):** Prints `"Invalid Choice!"`.

In both search modes, it prints `"Element found at position <pos>"` (1-based) if found, or `"Element not found."` if missing.

### Sample Run (Choosing Binary Search)
```text
Enter the number of elements: 5
Enter the elements: 4 8 12 16 20

----- MENU -----
1. Linear Search
2. Binary Search
Enter your choice: 2
Enter the element to search: 16
Element found at position 4
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term | Definition |
|---|---|
| **Menu-Driven Program** | An interactive program that presents numbered options to the user and executes the specific operation matching the user's numeric selection. |
| **`switch` Statement** | A multi-way selection control statement in C++ that jumps directly to the `case` label matching an integer/character expression (`choice`). |
| **`break` Statement** | Transfers control out of the enclosing `switch` (or loop) block immediately, preventing execution from **falling through** into the next `case`. |
| **`default` Label** | Optional catch-all branch inside a `switch` statement executed when no `case` constant matches the selector value. |
| **Linear Search** | Sequential `O(n)` element-by-element search with no sorting requirement. |
| **Binary Search** | Divide-and-conquer `O(log n)` interval-halving search requiring a **sorted** array. |
| **Block Scope (`{ ... }`)** | A pair of curly braces limiting the lifetime and scope of local variables declared inside a `switch` `case`. |

---

## 3. Core Facts, Rules & Uses

### Important Rules
1. **When to select Option `1` (Linear Search):** Whenever the input array is **unsorted** or very small.
2. **When to select Option `2` (Binary Search):** Only when the entered array is **already sorted in ascending order**.
3. **C++ `switch` Variable Scope Rule:** In C++, declaring and initializing new variables (`int low = 0, high = n - 1, mid;`) inside a `case` requires wrapping that `case` in **`{ ... }` curly braces**. Without braces, jumping directly to `default:` crosses variable initialization in the same scope and causes a C++ compilation error!

### Uses / Applications
1. **Menu-driven lab utilities & CLI tools** — letting users pick between algorithms based on data properties (unsorted vs. sorted).
2. **Database query engines** — choosing a full table scan (Linear Search) on unindexed columns vs. index search (Binary/B-Tree Search) on sorted/indexed columns.

---

## 4. Step-by-Step Algorithm

1. Start.
2. Read `n`, read `n` elements into `arr[0 .. n - 1]`.
3. Display the menu (`1. Linear Search`, `2. Binary Search`), read `choice`, and read `key`.
4. Evaluate `switch (choice)`:
   - **`case 1` (Linear Search):**
     - Loop `i` from `0` to `n - 1`: if `arr[i] == key`, print position `i + 1` and `return 0`.
     - Print `"Element not found."` and `break`.
   - **`case 2` (Binary Search):**
     - Set `low = 0`, `high = n - 1`.
     - While `low <= high`: set `mid = (low + high) / 2`; if `arr[mid] == key`, print position `mid + 1` and `return 0`; else if `arr[mid] < key`, set `low = mid + 1`; else set `high = mid - 1`.
     - Print `"Element not found."` and `break`.
   - **`default`:**
     - Print `"Invalid Choice!"`.
5. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
using namespace std;
int main() {
    int arr[10], n, key, choice;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "\n----- MENU -----\n1. Linear Search\n2. Binary Search\nEnter your choice: "; cin >> choice;
    cout << "Enter the element to search: "; cin >> key;
    switch (choice) {
        case 1:
            for (int i = 0; i < n; i++)
                if (arr[i] == key) { cout << "Element found at position " << i + 1; return 0; }
            cout << "Element not found."; break;
        case 2: {
            int low = 0, high = n - 1, mid;
            while (low <= high) {
                mid = (low + high) / 2;
                if (arr[mid] == key) { cout << "Element found at position " << mid + 1; return 0; }
                else if (arr[mid] < key) low = mid + 1;
                else high = mid - 1;
            }
            cout << "Element not found.";
            break;
        }
        default: cout << "Invalid Choice!";
    }
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `int arr[10], n, key, choice;` | Declares the 10-element array, active count `n`, search target `key`, and menu selector `choice`. |
| `for (int i = 0; i < n; i++) cin >> arr[i];` | Populates `arr[0 .. n - 1]` from keyboard input. |
| `cout << "\n----- MENU -----\n..."` | Prints the numbered menu using `\n` newline characters and reads `choice` and `key`. |
| `switch (choice)` | Transfers execution to `case 1`, `case 2`, or `default` depending on the integer `choice`. |
| `case 1:` | Runs Linear Search (`0 .. n - 1`). Exits via `return 0` if found; otherwise prints `"Element not found."` and hits `break;` to exit `switch`. |
| `case 2: { ... }` | Curly braces create a local scope for `low`, `high`, and `mid`, then run iterative Binary Search. |
| `default: cout << "Invalid Choice!";` | Handles any invalid menu number (anything other than `1` or `2`). |

---

## 6. Step-by-Step Dry Runs

### Case A — Choice `1` on Unsorted Data (`n = 4`, `arr = [25, 10, 40, 15]`, `key = 40`)
- Enters `case 1`:
  - `i = 0`: `25 != 40`
  - `i = 1`: `10 != 40`
  - `i = 2`: `40 == 40` → prints `Element found at position 3` and exits.

### Case B — Choice `2` on Sorted Data (`n = 5`, `arr = [4, 8, 12, 16, 20]`, `key = 16`)
- Enters `case 2`:
  - Step 1: `low = 0, high = 4 → mid = 2` (`arr[2] = 12 < 16` → `low = 3`).
  - Step 2: `low = 3, high = 4 → mid = 3` (`arr[3] = 16 == 16`) → prints `Element found at position 4` and exits.

---

## 7. Time & Space Complexity Comparison

| Metric / Property | Option 1: Linear Search | Option 2: Binary Search |
|---|---|---|
| **Prerequisite** | None (sorted or unsorted) | **Sorted array required** |
| **Best-Case Time Complexity** | **O(1)** (`arr[0] == key`) | **O(1)** (`arr[mid] == key` on first check) |
| **Average-Case Time Complexity** | **O(n)** | **O(log n)** |
| **Worst-Case Time Complexity** | **O(n)** | **O(log n)** |
| **Auxiliary Space Complexity** | **O(1)** | **O(1)** |
| **Total Space Complexity** | **O(n)** (array of `n` elements) | **O(n)** (array of `n` elements) |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Selecting Binary Search (`2`) on unsorted input:** Compiles without error, *but* eliminates the wrong half and outputs `"Element not found."`.
- **Mistake 2 — Omitting `{ }` around `case 2`:** Causes a C++ compile error because `int low = 0, high = n - 1` is initialized inside `switch` without its own block scope.
- **Mistake 3 — Omitting `break;` at the end of `case 1` or `case 2`:** Causes **case fall-through**, executing the next `case` / `default` block unintentionally.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Compare Linear Search and Binary Search on prerequisite and time complexity. | Linear Search needs **no sorting** and takes **O(n)** time; Binary Search requires a **sorted array** and takes **O(log n)** time. |
| 2 | State the space complexity of this program. | **O(1)** auxiliary space (and `O(n)` for storing the input array `arr`). |
| 3 | Why are `{ }` curly braces required around `case 2` in C++? | Because local variables (`low`, `high`, `mid`) are declared and initialized inside `case 2`; C++ forbids jumping past variable initializations to `default:` unless enclosed in a local block `{ }`. |
| 4 | What is the purpose of `break;` inside a `switch` statement? | It exits the `switch` block immediately so execution does not fall through into the following `case` or `default` label. |
| 5 | What does `default:` do in `switch (choice)`? | Executes whenever `choice` does not match any `case` constant (any input other than `1` or `2`). |
| 6 | Which data types are allowed inside `switch (expr)` in C++? | Only **integral or enumeration types** (`int`, `char`, `short`, `long`, `enum`) — NOT `float`, `double`, or `std::string`. |
| 7 | What happens if a user selects Binary Search (`2`) after entering `30 10 50 20`? | Binary Search may return an incorrect `"Element not found."` result because the input violates the sorted-order prerequisite. |
| 8 | What are the best-case time complexities of both options? | Both have **O(1)** best-case time: Linear Search when `key == arr[0]`, and Binary Search when `key == arr[(n-1)/2]`. |
| 9 | How would you make the menu repeat continuously until the user chooses Exit? | Wrap the menu and `switch` block inside a `do { ... } while (choice != 0);` loop and use a `bool found` flag instead of `return 0;`. |
| 10 | When is Option 1 preferable to Option 2? | When the input array is **unsorted** and we only need a quick search without changing element positions by sorting. |
