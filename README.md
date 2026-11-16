# DSA Practicals

Ten practicals. Each one is in its own folder with the program, a **theory note**
(what and why) and a **code explanation** (how the code works, dry run, viva).

| # | Practical | Language | Program | Notes |
|---|---|---|---|---|
| 1 | Student database — dynamic memory, Linear & Binary Search, Bubble & Selection Sort | C++ | [`student_database.cpp`](part_a_cpp/01-student-database-search-and-sort/student_database.cpp) | [theory](part_a_cpp/01-student-database-search-and-sort/THEORY.md) · [explanation](part_a_cpp/01-student-database-search-and-sort/EXPLANATION.md) |
| 2 | Stack ADT on a linked list + infix → postfix / prefix | C++ | [`stack_conversions.cpp`](part_a_cpp/02-stack-infix-postfix-prefix/stack_conversions.cpp) | [theory](part_a_cpp/02-stack-infix-postfix-prefix/THEORY.md) · [explanation](part_a_cpp/02-stack-infix-postfix-prefix/EXPLANATION.md) |
| 3 | Circular Queue on an array — enqueue, dequeue, display, full check | C++ | [`circular_queue.cpp`](part_a_cpp/03-circular-queue-array/circular_queue.cpp) | [theory](part_a_cpp/03-circular-queue-array/THEORY.md) · [explanation](part_a_cpp/03-circular-queue-array/EXPLANATION.md) |
| 4 | Binary Search Tree — insert, delete, search, traversals, depth, mirror, copy, parents, leaves, level-wise | Python | [`binary_search_tree.py`](part_b_python/04-binary-search-tree/binary_search_tree.py) | [theory](part_b_python/04-binary-search-tree/THEORY.md) · [explanation](part_b_python/04-binary-search-tree/EXPLANATION.md) |
| 5 | Campus graph + MST with Kruskal and Prim | Python | [`campus_mst.py`](part_b_python/05-campus-graph-mst-kruskal-prim/campus_mst.py) | [theory](part_b_python/05-campus-graph-mst-kruskal-prim/THEORY.md) · [explanation](part_b_python/05-campus-graph-mst-kruskal-prim/EXPLANATION.md) |
| 6 | Heap Sort | Python | [`heap_sort.py`](part_b_python/06-heap-sort/heap_sort.py) | [theory](part_b_python/06-heap-sort/THEORY.md) · [explanation](part_b_python/06-heap-sort/EXPLANATION.md) |
| 7 | Merge Sort — online orders by delivery time | Python | [`merge_sort_orders.py`](part_b_python/07-merge-sort-orders/merge_sort_orders.py) | [theory](part_b_python/07-merge-sort-orders/THEORY.md) · [explanation](part_b_python/07-merge-sort-orders/EXPLANATION.md) |
| 8 | Fractional Knapsack (greedy) — maximise shipping profit | Python | [`fractional_knapsack.py`](part_b_python/08-fractional-knapsack/fractional_knapsack.py) | [theory](part_b_python/08-fractional-knapsack/THEORY.md) · [explanation](part_b_python/08-fractional-knapsack/EXPLANATION.md) |
| 9 | Naïve string matching — all occurrences of a pattern | Python | [`naive_string_matching.py`](part_b_python/09-naive-string-matching/naive_string_matching.py) | [theory](part_b_python/09-naive-string-matching/THEORY.md) · [explanation](part_b_python/09-naive-string-matching/EXPLANATION.md) |
| 10 | Maze navigation — BFS, A\*, dynamic re-planning, visualisation | Python | [`maze_ai_search.py`](part_b_python/10-maze-ai-search/maze_ai_search.py) | [theory](part_b_python/10-maze-ai-search/THEORY.md) · [explanation](part_b_python/10-maze-ai-search/EXPLANATION.md) |

## Run

**C++ (1–3)** — compile and run inside the practical's folder:

```bash
cd part_a_cpp/01-student-database-search-and-sort
g++ student_database.cpp -o student_database && ./student_database
```

**Python (4–10)** — no installation, standard library only:

```bash
cd part_b_python/06-heap-sort
python3 heap_sort.py
```

4, 5 and 10 have a menu; 6, 7, 8 and 9 run their demo directly.

## Verify everything

```bash
bash check_all.sh
```

Compiles the 3 C++ programs and syntax-checks the 7 Python ones →
`passed: 10   failed: 0`.

## Complexity at a glance

| Algorithm | Time | Space |
|---|---|---|
| Linear search | O(n) | O(1) |
| Binary search (sorted) | O(log n) | O(1) |
| Bubble / Selection sort | O(n²) | O(1) |
| Stack push / pop | O(1) | O(1) per node |
| Infix → postfix / prefix | O(n) | O(n) |
| Circular queue enqueue / dequeue | O(1) | O(SIZE) |
| BST insert / search / delete | O(log n) avg, O(n) worst | O(n) |
| Kruskal / Prim (MST) | O(E log E) / O(E log V) | O(V + E) |
| Heap sort | O(n log n) | O(1) |
| Merge sort | O(n log n) | O(n) |
| Fractional knapsack | O(n log n) | O(n) |
| Naïve string matching | O(n·m) | O(1) |
| BFS / A\* on a maze | O(V+E) / O(E log V) | O(V) |

## Layout

```
part_a_cpp/01-student-database-search-and-sort/   student_database.cpp, THEORY.md, EXPLANATION.md
part_a_cpp/02-stack-infix-postfix-prefix/         stack_conversions.cpp, THEORY.md, EXPLANATION.md
part_a_cpp/03-circular-queue-array/               circular_queue.cpp, THEORY.md, EXPLANATION.md
part_b_python/04-binary-search-tree/              binary_search_tree.py, THEORY.md, EXPLANATION.md
part_b_python/05-campus-graph-mst-kruskal-prim/   campus_mst.py, THEORY.md, EXPLANATION.md
part_b_python/06-heap-sort/                       heap_sort.py, THEORY.md, EXPLANATION.md
part_b_python/07-merge-sort-orders/               merge_sort_orders.py, THEORY.md, EXPLANATION.md
part_b_python/08-fractional-knapsack/             fractional_knapsack.py, THEORY.md, EXPLANATION.md
part_b_python/09-naive-string-matching/           naive_string_matching.py, THEORY.md, EXPLANATION.md
part_b_python/10-maze-ai-search/                  maze_ai_search.py, THEORY.md, EXPLANATION.md
check_all.sh
```
