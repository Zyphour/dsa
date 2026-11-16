# Practical 1 — Student Database (Searching & Sorting)

**Aim:** Store student records (ID, Name, CGPA) in memory allocated at run time,
grow the list with `realloc()`, search by ID using Linear and Binary Search, sort
by Name and CGPA, and compare search cost before and after sorting.

**Language:** C++ · **Program:** [`student_database.cpp`](student_database.cpp)

---

## Concepts

- **struct** – one record that keeps ID, name and CGPA together.
- **Static memory** – `Student db[100];` fixes the size at compile time.
- **Dynamic memory** – `malloc`/`realloc` let the list grow while the program runs.
- `realloc(p, n)` resizes the block and may move it, so always keep the returned pointer.
- Records are moved as a whole struct, never field by field, so the three values never get mixed up.

## Searching

**Linear search — O(n).** Compare records one by one from index 0. Works on any
order. Average `n/2` comparisons, worst `n`.

**Binary search — O(log n).** Works only on data **sorted by ID**. Compare with
the middle record: if the target is bigger go right, if smaller go left, repeat.
Each step throws away half the records.

| n | worst comparisons (binary) |
|---|---|
| 100 | 7 |
| 1,000 | 10 |
| 1,00,000 | 17 |

## Sorting

**Bubble sort (by Name, by ID).** Swap neighbouring records when they are in the
wrong order; after every pass the largest value sits at the end. If a pass makes
no swap the array is already sorted, so the best case is `O(n)`.
Names are compared with `strcmp`.

**Selection sort (by CGPA, ascending or descending).** Find the best record in
the unsorted part and swap it to the front. Always `O(n²)` comparisons, but at
most `n−1` swaps.

| Sort | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | no |

## Analysis: searching before vs after sorting

The program makes a copy, bubble-sorts it by ID, then searches the same IDs with
both algorithms and counts comparisons:

```
Total comparisons   Linear = 20   Binary = 13
```

Why binary search wins:

1. Linear search checks up to `n` records, binary search at most `log2 n`.
2. The gap grows with `n` — this is the point of sorting.
3. Binary search is **only** valid on data sorted by the searched key.
4. Sorting is a one-time cost (`O(n log n)` for a good sort, `O(n²)` for bubble/selection here); after that every search is cheap.

## Exam points

- Binary search on unsorted data gives wrong answers; it must be sorted by ID.
- `realloc` can fail (`NULL`) — check before overwriting the old pointer.
- Memory obtained with `malloc`/`realloc` must be released with `free`.
- Search *many* times → sort once and use binary search. Search *once* → linear search is enough.
