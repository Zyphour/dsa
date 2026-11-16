# DSA Experiments

C++ and Python implementations of core Data Structures & Algorithms, organized
directly by experiment folder at the repository root. Every program comes with:

- **Program** — the C++ or Python source file
- **Theory** — written lab info to submit with the program (aim, topic overview, how it works, algorithm, complexity)
- **Explanation** — complete, fact-focused reference covering what the code does, definitions, full forms, uses/applications, step-by-step algorithm, line-by-line code guide, dry runs, time & space complexity, common mistakes, and straightforward viva Q&A

## All Programs

| # | Program / Experiment | Language | Program | Theory | Explanation | Section |
|---|---|---|---|---|---|---|
| 00a | Linear Search | C++ | [`linear_search.cpp`](00a-linear-search/linear_search.cpp) | [theory](00a-linear-search/THEORY.md) | [explanation](00a-linear-search/EXPLANATION.md) | [jump](#00a-linear-search) |
| 00b | Binary Search | C++ | [`binary_search.cpp`](00b-binary-search/binary_search.cpp) | [theory](00b-binary-search/THEORY.md) | [explanation](00b-binary-search/EXPLANATION.md) | [jump](#00b-binary-search) |
| 00c | Linear & Binary Search (Menu) | C++ | [`linear_binary_search.cpp`](00c-linear-binary-search/linear_binary_search.cpp) | [theory](00c-linear-binary-search/THEORY.md) | [explanation](00c-linear-binary-search/EXPLANATION.md) | [jump](#00c-linear--binary-search-menu) |
| 00d | Bubble Sort | C++ | [`bubble_sort.cpp`](00d-bubble-sort/bubble_sort.cpp) | [theory](00d-bubble-sort/THEORY.md) | [explanation](00d-bubble-sort/EXPLANATION.md) | [jump](#00d-bubble-sort) |
| 00e | Selection Sort | C++ | [`selection_sort.cpp`](00e-selection-sort/selection_sort.cpp) | [theory](00e-selection-sort/THEORY.md) | [explanation](00e-selection-sort/EXPLANATION.md) | [jump](#00e-selection-sort) |
| 00f | Insertion Sort | C++ | [`insertion_sort.cpp`](00f-insertion-sort/insertion_sort.cpp) | [theory](00f-insertion-sort/THEORY.md) | [explanation](00f-insertion-sort/EXPLANATION.md) | [jump](#00f-insertion-sort) |
| 01 | Student Database (Bubble Sort on structs) | C++ | [`student_database.cpp`](01-student-database-search-and-sort/student_database.cpp) | [theory](01-student-database-search-and-sort/THEORY.md) | [explanation](01-student-database-search-and-sort/EXPLANATION.md) | [jump](#01-student-database) |
| 02 | Stack ADT (Linked List) + Infix → Postfix / Prefix | C++ | [`stack_conversions.cpp`](02-stack-infix-postfix-prefix/stack_conversions.cpp) | [theory](02-stack-infix-postfix-prefix/THEORY.md) | [explanation](02-stack-infix-postfix-prefix/EXPLANATION.md) | [jump](#02-stack-adt--expression-conversion) |
| 03 | Circular Queue on Array | C++ | [`circular_queue.cpp`](03-circular-queue-array/circular_queue.cpp) | [theory](03-circular-queue-array/THEORY.md) | [explanation](03-circular-queue-array/EXPLANATION.md) | [jump](#03-circular-queue) |
| 04 | Binary Search Tree (BST) | Python | [`binary_search_tree.py`](04-binary-search-tree/binary_search_tree.py) | [theory](04-binary-search-tree/THEORY.md) | [explanation](04-binary-search-tree/EXPLANATION.md) | [jump](#04-binary-search-tree) |
| 05 | Campus Graph + Kruskal & Prim MST | Python | [`campus_mst.py`](05-campus-graph-mst-kruskal-prim/campus_mst.py) | [theory](05-campus-graph-mst-kruskal-prim/THEORY.md) | [explanation](05-campus-graph-mst-kruskal-prim/EXPLANATION.md) | [jump](#05-campus-graph--mst) |
| 06 | Heap Sort | Python | [`heap_sort.py`](06-heap-sort/heap_sort.py) | [theory](06-heap-sort/THEORY.md) | [explanation](06-heap-sort/EXPLANATION.md) | [jump](#06-heap-sort) |
| 07 | Merge Sort | Python | [`merge_sort_orders.py`](07-merge-sort-orders/merge_sort_orders.py) | [theory](07-merge-sort-orders/THEORY.md) | [explanation](07-merge-sort-orders/EXPLANATION.md) | [jump](#07-merge-sort) |
| 08 | Fractional Knapsack (Greedy) | Python | [`fractional_knapsack.py`](08-fractional-knapsack/fractional_knapsack.py) | [theory](08-fractional-knapsack/THEORY.md) | [explanation](08-fractional-knapsack/EXPLANATION.md) | [jump](#08-fractional-knapsack) |
| 09 | Naïve String Matching | Python | [`naive_string_matching.py`](09-naive-string-matching/naive_string_matching.py) | [theory](09-naive-string-matching/THEORY.md) | [explanation](09-naive-string-matching/EXPLANATION.md) | [jump](#09-naïve-string-matching) |
| 10 | Maze Navigation (BFS, A\*, Dynamic Re-planning) | Python | [`maze_ai_search.py`](10-maze-ai-search/maze_ai_search.py) | [theory](10-maze-ai-search/THEORY.md) | [explanation](10-maze-ai-search/EXPLANATION.md) | [jump](#10-maze-ai-search) |

---

## Programs (Dedicated Sections)

### 00a. Linear Search
Sequential search over 5 integers.
- **Program:** [`00a-linear-search/linear_search.cpp`](00a-linear-search/linear_search.cpp)
- **Theory:** [`00a-linear-search/THEORY.md`](00a-linear-search/THEORY.md)
- **Explanation:** [`00a-linear-search/EXPLANATION.md`](00a-linear-search/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 00a-linear-search/linear_search.cpp -o /tmp/linear_search && /tmp/linear_search
  ```

---

### 00b. Binary Search
Divide-and-conquer search on a sorted array.
- **Program:** [`00b-binary-search/binary_search.cpp`](00b-binary-search/binary_search.cpp)
- **Theory:** [`00b-binary-search/THEORY.md`](00b-binary-search/THEORY.md)
- **Explanation:** [`00b-binary-search/EXPLANATION.md`](00b-binary-search/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 00b-binary-search/binary_search.cpp -o /tmp/binary_search && /tmp/binary_search
  ```

---

### 00c. Linear & Binary Search (Menu)
Menu-driven choice between Linear Search and Binary Search.
- **Program:** [`00c-linear-binary-search/linear_binary_search.cpp`](00c-linear-binary-search/linear_binary_search.cpp)
- **Theory:** [`00c-linear-binary-search/THEORY.md`](00c-linear-binary-search/THEORY.md)
- **Explanation:** [`00c-linear-binary-search/EXPLANATION.md`](00c-linear-binary-search/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 00c-linear-binary-search/linear_binary_search.cpp -o /tmp/linear_binary_search && /tmp/linear_binary_search
  ```

---

### 00d. Bubble Sort
Adjacent-swap ascending sort.
- **Program:** [`00d-bubble-sort/bubble_sort.cpp`](00d-bubble-sort/bubble_sort.cpp)
- **Theory:** [`00d-bubble-sort/THEORY.md`](00d-bubble-sort/THEORY.md)
- **Explanation:** [`00d-bubble-sort/EXPLANATION.md`](00d-bubble-sort/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 00d-bubble-sort/bubble_sort.cpp -o /tmp/bubble_sort && /tmp/bubble_sort
  ```

---

### 00e. Selection Sort
Repeatedly selects the minimum from the unsorted suffix and swaps into place.
- **Program:** [`00e-selection-sort/selection_sort.cpp`](00e-selection-sort/selection_sort.cpp)
- **Theory:** [`00e-selection-sort/THEORY.md`](00e-selection-sort/THEORY.md)
- **Explanation:** [`00e-selection-sort/EXPLANATION.md`](00e-selection-sort/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 00e-selection-sort/selection_sort.cpp -o /tmp/selection_sort && /tmp/selection_sort
  ```

---

### 00f. Insertion Sort
Inserts each element into its sorted prefix position by shifting larger elements right.
- **Program:** [`00f-insertion-sort/insertion_sort.cpp`](00f-insertion-sort/insertion_sort.cpp)
- **Theory:** [`00f-insertion-sort/THEORY.md`](00f-insertion-sort/THEORY.md)
- **Explanation:** [`00f-insertion-sort/EXPLANATION.md`](00f-insertion-sort/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 00f-insertion-sort/insertion_sort.cpp -o /tmp/insertion_sort && /tmp/insertion_sort
  ```

---

### 01. Student Database
Reads 15 student records (`roll`, `name`, `cgpa`) and sorts them by roll number using Bubble Sort.
- **Program:** [`01-student-database-search-and-sort/student_database.cpp`](01-student-database-search-and-sort/student_database.cpp)
- **Theory:** [`01-student-database-search-and-sort/THEORY.md`](01-student-database-search-and-sort/THEORY.md)
- **Explanation:** [`01-student-database-search-and-sort/EXPLANATION.md`](01-student-database-search-and-sort/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 01-student-database-search-and-sort/student_database.cpp -o /tmp/student_database && /tmp/student_database
  ```

---

### 02. Stack ADT & Expression Conversion
Singly linked-list Stack with push/pop/display and infix → postfix / prefix conversion.
- **Program:** [`02-stack-infix-postfix-prefix/stack_conversions.cpp`](02-stack-infix-postfix-prefix/stack_conversions.cpp)
- **Theory:** [`02-stack-infix-postfix-prefix/THEORY.md`](02-stack-infix-postfix-prefix/THEORY.md)
- **Explanation:** [`02-stack-infix-postfix-prefix/EXPLANATION.md`](02-stack-infix-postfix-prefix/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 02-stack-infix-postfix-prefix/stack_conversions.cpp -o /tmp/stack_conversions && /tmp/stack_conversions
  ```

---

### 03. Circular Queue
Array-based circular queue of size 5 supporting enqueue, dequeue, and display.
- **Program:** [`03-circular-queue-array/circular_queue.cpp`](03-circular-queue-array/circular_queue.cpp)
- **Theory:** [`03-circular-queue-array/THEORY.md`](03-circular-queue-array/THEORY.md)
- **Explanation:** [`03-circular-queue-array/EXPLANATION.md`](03-circular-queue-array/EXPLANATION.md)
- **Run:**
  ```bash
  g++ -Wall -O2 03-circular-queue-array/circular_queue.cpp -o /tmp/circular_queue && /tmp/circular_queue
  ```

---

### 04. Binary Search Tree
Binary Search Tree supporting insert, search, delete, and inorder traversal.
- **Program:** [`04-binary-search-tree/binary_search_tree.py`](04-binary-search-tree/binary_search_tree.py)
- **Theory:** [`04-binary-search-tree/THEORY.md`](04-binary-search-tree/THEORY.md)
- **Explanation:** [`04-binary-search-tree/EXPLANATION.md`](04-binary-search-tree/EXPLANATION.md)
- **Run:**
  ```bash
  python3 04-binary-search-tree/binary_search_tree.py
  ```

---

### 05. Campus Graph & MST
Represents a 5-building campus graph using both adjacency list and adjacency matrix, then finds the Minimum Spanning Tree using Kruskal's and Prim's algorithms.
- **Program:** [`05-campus-graph-mst-kruskal-prim/campus_mst.py`](05-campus-graph-mst-kruskal-prim/campus_mst.py)
- **Theory:** [`05-campus-graph-mst-kruskal-prim/THEORY.md`](05-campus-graph-mst-kruskal-prim/THEORY.md)
- **Explanation:** [`05-campus-graph-mst-kruskal-prim/EXPLANATION.md`](05-campus-graph-mst-kruskal-prim/EXPLANATION.md)
- **Run:**
  ```bash
  python3 05-campus-graph-mst-kruskal-prim/campus_mst.py
  ```

---

### 06. Heap Sort
Sorts a list in place by building a max-heap and repeatedly extracting the maximum.
- **Program:** [`06-heap-sort/heap_sort.py`](06-heap-sort/heap_sort.py)
- **Theory:** [`06-heap-sort/THEORY.md`](06-heap-sort/THEORY.md)
- **Explanation:** [`06-heap-sort/EXPLANATION.md`](06-heap-sort/EXPLANATION.md)
- **Run:**
  ```bash
  python3 06-heap-sort/heap_sort.py
  ```

---

### 07. Merge Sort
Recursive divide-and-conquer Merge Sort demo.
- **Program:** [`07-merge-sort-orders/merge_sort_orders.py`](07-merge-sort-orders/merge_sort_orders.py)
- **Theory:** [`07-merge-sort-orders/THEORY.md`](07-merge-sort-orders/THEORY.md)
- **Explanation:** [`07-merge-sort-orders/EXPLANATION.md`](07-merge-sort-orders/EXPLANATION.md)
- **Run:**
  ```bash
  python3 07-merge-sort-orders/merge_sort_orders.py
  ```

---

### 08. Fractional Knapsack
Greedy Fractional Knapsack choosing items by highest profit-to-weight ratio.
- **Program:** [`08-fractional-knapsack/fractional_knapsack.py`](08-fractional-knapsack/fractional_knapsack.py)
- **Theory:** [`08-fractional-knapsack/THEORY.md`](08-fractional-knapsack/THEORY.md)
- **Explanation:** [`08-fractional-knapsack/EXPLANATION.md`](08-fractional-knapsack/EXPLANATION.md)
- **Run:**
  ```bash
  python3 08-fractional-knapsack/fractional_knapsack.py
  ```

---

### 09. Naïve String Matching
Finds all occurrences (including overlaps) of a pattern inside a text string.
- **Program:** [`09-naive-string-matching/naive_string_matching.py`](09-naive-string-matching/naive_string_matching.py)
- **Theory:** [`09-naive-string-matching/THEORY.md`](09-naive-string-matching/THEORY.md)
- **Explanation:** [`09-naive-string-matching/EXPLANATION.md`](09-naive-string-matching/EXPLANATION.md)
- **Run:**
  ```bash
  python3 09-naive-string-matching/naive_string_matching.py
  ```

---

### 10. Maze AI Search
Solves a 7 × 11 grid maze using BFS, A\* (Manhattan heuristic), and dynamic re-planning when a wall blocks the path mid-walk.
- **Program:** [`10-maze-ai-search/maze_ai_search.py`](10-maze-ai-search/maze_ai_search.py)
- **Theory:** [`10-maze-ai-search/THEORY.md`](10-maze-ai-search/THEORY.md)
- **Explanation:** [`10-maze-ai-search/EXPLANATION.md`](10-maze-ai-search/EXPLANATION.md)
- **Run:**
  ```bash
  python3 10-maze-ai-search/maze_ai_search.py
  ```

---

## Verify Everything

```bash
bash check_all.sh
```

Compiles all 9 C++ programs (`g++ -Wall -O2`) and syntax-checks all 7 Python
programs (`python3 -m py_compile`) → `passed: 16   failed: 0`.

## Complexity at a Glance

| Algorithm | Time | Space |
|---|---|---|
| Linear search | O(n) | O(1) |
| Binary search (sorted) | O(log n) | O(1) |
| Bubble / Selection sort | O(n²) | O(1) |
| Insertion sort | O(n) best, O(n²) worst | O(1) |
| Stack push / pop | O(1) | O(1) per node |
| Infix → postfix / prefix | O(n) | O(n) |
| Circular queue enqueue / dequeue | O(1) | O(SIZE) |
| BST insert / search / delete | O(log n) avg, O(n) worst | O(n) |
| Kruskal / Prim (MST) | O(E log E) / O(V·E) | O(V + E) |
| Heap sort | O(n log n) | O(1) |
| Merge sort | O(n log n) | O(n) |
| Fractional knapsack | O(n log n) | O(1) extra |
| Naïve string matching | O(n · m) | O(1) |
| BFS / A\* on a maze | O(V + E) / O(E log V) | O(V) |

## Repository Layout

```text
.
├── check_all.sh
├── 00a-linear-search/
│   ├── linear_search.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 00b-binary-search/
│   ├── binary_search.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 00c-linear-binary-search/
│   ├── linear_binary_search.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 00d-bubble-sort/
│   ├── bubble_sort.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 00e-selection-sort/
│   ├── selection_sort.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 00f-insertion-sort/
│   ├── insertion_sort.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 01-student-database-search-and-sort/
│   ├── student_database.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 02-stack-infix-postfix-prefix/
│   ├── stack_conversions.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 03-circular-queue-array/
│   ├── circular_queue.cpp
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 04-binary-search-tree/
│   ├── binary_search_tree.py
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 05-campus-graph-mst-kruskal-prim/
│   ├── campus_mst.py
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 06-heap-sort/
│   ├── heap_sort.py
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 07-merge-sort-orders/
│   ├── merge_sort_orders.py
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 08-fractional-knapsack/
│   ├── fractional_knapsack.py
│   ├── EXPLANATION.md
│   └── THEORY.md
├── 09-naive-string-matching/
│   ├── naive_string_matching.py
│   ├── EXPLANATION.md
│   └── THEORY.md
└── 10-maze-ai-search/
    ├── maze_ai_search.py
    ├── EXPLANATION.md
    └── THEORY.md
```
