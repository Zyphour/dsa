# Practical 1 — Student Database

**Aim:** Store 15 student records (`roll`, `name`, `cgpa`) using a C++ `struct`
and sort them in ascending order of roll number using Bubble Sort.

**Language:** C++ · **Program:** [`student_database.cpp`](student_database.cpp)

---

## Concepts

- **`struct`** – bundles fields of different types (`int roll`, `string name`,
  `float cgpa`) into one `Student` record.
- **Record sorting** – comparisons use a single key field (`s[j].roll`), while
  swaps move the **entire `Student` struct** so each student keeps their own
  name and CGPA.

## Algorithm

1. Define `struct Student { int roll; string name; float cgpa; };`.
2. Declare `Student s[15]` and `temp`, then read all 15 records.
3. For `i = 0` to `13`:
   - For `j = 0` to `13 - i`:
     - If `s[j].roll > s[j + 1].roll`, swap `s[j]` and `s[j + 1]` using `temp`.
4. Print all 15 records in sorted order.

## Complexity

| Metric | Value | Why |
|---|---|---|
| Time | O(n²) | Two nested Bubble Sort loops (`n = 15`) |
| Space | O(1) extra | In-place swap using one `temp` struct |

## Exam points

- Assigning `temp = s[j]` in C++ copies all struct fields together automatically.
- Swapping only `.roll` instead of the whole struct would corrupt the database.
- `cin >> s[i].name` reads single-word names without spaces.
