# Practical 1: Student Database — Complete Reference & Code Guide (`student_database.cpp`)

> **Aim:** Store 15 student records (`roll`, `name`, `cgpa`) using a C++ `struct` and sort them in ascending order of roll number using Bubble Sort.
>
> **Language:** C++ · **Program:** [`student_database.cpp`](student_database.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`student_database.cpp`](student_database.cpp) defines a `Student` structure with three fields (`int roll`, `string name`, `float cgpa`), reads **15 student records** from standard input into an array `Student s[15]`, sorts all 15 records **in ascending order of `roll` number** using **Bubble Sort** (moving entire `Student` records during each swap so names and CGPAs stay matched to their roll numbers), and prints all 15 sorted records line by line.

### Sample Input & Output Pattern (Illustrated with 3 Records)
**Input:**
```text
103 Neha 8.9
101 Aman 9.2
102 Riya 8.5
```
**Output:**
```text
101 Aman 9.2
102 Riya 8.5
103 Neha 8.9
```
*(In the actual program, `15` student lines are read and `15` sorted lines are printed.)*

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Definition |
|---|---|
| **`struct` (Structure)** | A user-defined composite data type in C/C++ that groups variables of **different data types** (members/fields) under a single name to represent one logical record. |
| **Record** | A collection of related fields describing one entity (here, one student: `roll`, `name`, `cgpa`). |
| **Field (Member)** | An individual attribute inside a `struct`, accessed via the dot operator `.` (e.g., `s[i].roll`). |
| **Array of Structures** | A contiguous array where every element is a `struct` object (`Student s[15]`), used to store a table/database of records in memory. |
| **Sorting Key** | The specific field of a record used for comparison during sorting (here `s[j].roll`). |
| **CGPA** | **Full Form:** *Cumulative Grade Point Average* (stored as `float` for decimal values like `8.9`). |
| **Memberwise Assignment** | C++ feature where `temp = s[j];` automatically copies **all fields** (`roll`, `name`, `cgpa`) from one struct variable to another of the same type. |

---

## 3. Core Facts, Rules, Advantages & Uses

### Key Rules of Record Sorting
1. **Compare ONE key field, Swap the ENTIRE `struct`:**
   - Comparison checks only `.roll`: `if (s[j].roll > s[j + 1].roll)`.
   - Swap copies the whole `Student` object: `temp = s[j]; s[j] = s[j + 1]; s[j + 1] = temp;`.
   - Swapping only `.roll` would corrupt the database by detaching roll numbers from their owners' names and CGPAs!
2. **Why `struct` is Superior to Parallel Arrays:**
   - Using 3 separate arrays (`roll[15]`, `name[15]`, `cgpa[15]`) requires 3 separate swaps and is error-prone. Grouping fields in `struct Student` keeps each record cohesive and swaps in 1 step.
3. **Stability Matters in Databases:**
   - Because Bubble Sort uses strict `>` (`s[j].roll > s[j + 1].roll`), it is **stable**: records with equal sort keys (e.g., if sorting by CGPA or department) preserve their previous order.

### Uses / Applications of Array of `struct` + Record Sorting
1. **Student / Employee / Inventory management systems** (in-memory tables sorted by ID, name, salary, or marks).
2. Preparing unsorted records so **Binary Search (`O(log n)`)** can later look up any student by roll number rapidly.
3. Generating **rank lists** (sorting by CGPA descending) or **attendance sheets** (sorting by roll number ascending).

---

## 4. Step-by-Step Algorithm

1. Start.
2. Define `struct Student { int roll; string name; float cgpa; };`.
3. Declare `Student s[15]` and `Student temp`.
4. Loop `i = 0` to `14`: read `s[i].roll`, `s[i].name`, and `s[i].cgpa`.
5. Run Bubble Sort on `s[0 .. 14]` (`n = 15`, so `n - 1 = 14`):
   - For `i = 0` to `13` (`i < 14`):
     - For `j = 0` to `13 - i` (`j < 14 - i`):
       - If `s[j].roll > s[j + 1].roll`, swap whole structs `s[j]` and `s[j + 1]` via `temp`.
6. Loop `i = 0` to `14`: print `s[i].roll`, `s[i].name`, and `s[i].cgpa`.
7. Stop.

---

## 5. Line-by-Line Code Explanation

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Student { int roll; string name; float cgpa; };

int main() {
    Student s[15], temp;
    for(int i=0; i<15; i++) cin >> s[i].roll >> s[i].name >> s[i].cgpa;
    for(int i=0; i<14; i++)
        for(int j=0; j<14-i; j++)
            if(s[j].roll > s[j+1].roll) { temp = s[j]; s[j] = s[j+1]; s[j+1] = temp; }
    for(int i=0; i<15; i++)
        cout << s[i].roll << " " << s[i].name << " " << s[i].cgpa << endl;
    return 0;
}
```

| Line(s) | Exact Role in the Program |
|---|---|
| `#include <string>` | Includes C++ `std::string` class needed for `name`. |
| `struct Student { int roll; string name; float cgpa; };` | Declares the composite `Student` record type. Note the **mandatory semicolon `;`** after `}`. |
| `Student s[15], temp;` | Creates an array of 15 `Student` records and one `Student` variable `temp` for swapping. |
| `for(int i=0; i<15; i++) cin >> s[i].roll >> s[i].name >> s[i].cgpa;` | Reads 15 records (`roll`, single-word `name`, `cgpa`). |
| `for(int i=0; i<14; i++)` | Outer Bubble Sort loop: `n - 1 = 15 - 1 = 14` passes (`i = 0..13`). |
| `for(int j=0; j<14-i; j++)` | Inner Bubble Sort loop: `n - 1 - i = 14 - i` adjacent comparisons per pass. |
| `if(s[j].roll > s[j+1].roll)` | Compares roll numbers of adjacent student records. |
| `{ temp = s[j]; s[j] = s[j+1]; s[j+1] = temp; }` | Swaps the **entire `Student` structures** (all 3 fields move together). |
| `cout << s[i].roll << " " << s[i].name << " " << s[i].cgpa << endl;` | Prints each sorted student record on its own line (`endl` outputs newline and flushes output). |

---

## 6. Step-by-Step Dry Run (Traced on 3 Records for Clarity)

**Initial Array:** `s = [(103, "Neha", 8.9), (101, "Aman", 9.2), (102, "Riya", 8.5)]`

| Pass `i` | `j` | Roll Check `s[j].roll > s[j+1].roll` | Action | Array `s` After Step |
|---|---|---|---|---|
| `i = 0` | `0` | `103 > 101` (True) | Swap `s[0] ↔ s[1]` | `[(101, Aman, 9.2), (103, Neha, 8.9), (102, Riya, 8.5)]` |
| `i = 0` | `1` | `103 > 102` (True) | Swap `s[1] ↔ s[2]` | `[(101, Aman, 9.2), (102, Riya, 8.5) \| (103, Neha, 8.9)]` |
| `i = 1` | `0` | `101 > 102` (False) | No swap | `[(101, Aman, 9.2) \| (102, Riya, 8.5), (103, Neha, 8.9)]` |

---

## 7. Time & Space Complexity Fact Sheet

For `n` student records (`n = 15` in this code):

| Metric | Complexity | Value / Explanation |
|---|---|---|
| **Best-Case Time Complexity** | **O(n²)** | `15 × 14 / 2 = 105` comparisons (no early-exit flag used). |
| **Average-Case Time Complexity** | **O(n²)** | `n(n - 1) / 2` comparisons. |
| **Worst-Case Time Complexity** | **O(n²)** | `105` comparisons and `105` whole-struct swaps (reverse-sorted roll numbers). |
| **Auxiliary Space Complexity** | **O(1)** | Only **1** extra `Student` struct (`temp`) plus loop counters `i`, `j`. |
| **Total Space Complexity** | **O(n)** | Stores `n = 15` `Student` records in `s[15]`. |
| **In-Place? / Stable?** | **Yes / Yes** | Sorts inside `s[]` and preserves relative order of equal keys. |

---

## 8. Quick Modifications & Common Mistakes

- **Sort by CGPA (Highest First):** Change condition to `if (s[j].cgpa < s[j+1].cgpa)`.
- **Sort by Name (Alphabetical A → Z):** Change condition to `if (s[j].name > s[j+1].name)`.
- **Mistake 1 — Swapping `s[j].roll` instead of `s[j]`:** Mixes roll numbers with wrong names and CGPAs!
- **Mistake 2 — Entering spaces in `name` (`Aman Verma`):** `cin >> s[i].name` stops at whitespace, causing `"Verma"` to be read into the `float cgpa` field and breaking input! Always enter single-word names (`Aman` or `Aman_Verma`).
- **Mistake 3 — Omitting `;` after `struct Student { ... };`:** Causes a C++ syntax error.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define a `struct` in C++. | A `struct` is a user-defined composite data type that groups variables of different data types under one name to represent a record. |
| 2 | Differentiate between an Array and a Structure (`struct`). | An **array** stores multiple elements of the **same** data type accessed by index; a **`struct`** groups fields of **different** data types accessed by member name (`.`). |
| 3 | Differentiate between `struct` and `class` in C++. | Members of a `struct` are **`public` by default**, whereas members of a `class` are **`private` by default**. |
| 4 | What is the full form of CGPA? | **Cumulative Grade Point Average**. |
| 5 | Why do we declare `temp` as type `Student` instead of `int`? | Because we must swap the **entire `Student` record** (`roll`, `name`, `cgpa`), not just the integer `roll`. |
| 6 | What happens if you swap only `s[j].roll` and `s[j+1].roll`? | Roll numbers change places while names and CGPAs stay put, corrupting every moved student's record. |
| 7 | State the time complexity and auxiliary space complexity of sorting `n` student records here. | Time complexity: **O(n²)**; Auxiliary space complexity: **O(1)**. |
| 8 | Why do the loops use `14` and `14 - i` when there are `15` students? | In Bubble Sort for `n = 15` items, `n - 1 = 14` passes are needed, and pass `i` checks `n - 1 - i = 14 - i` pairs. |
| 9 | How many comparisons are executed for `15` students? | `15 × 14 / 2 =` **105 comparisons**. |
| 10 | How would you modify the program to sort students in descending order of CGPA? | Replace `if (s[j].roll > s[j+1].roll)` with `if (s[j].cgpa < s[j+1].cgpa)`. |
| 11 | Why does `cin >> s[i].name` require single-word names? | The extraction operator `>>` treats spaces as delimiters and stops reading at the first space. (Full names with spaces require `getline()`.) |
| 12 | Once `s[15]` is sorted by `roll`, which search algorithm finds a roll number fastest and in what time? | **Binary Search**, in **O(log n)** time (at most 4 comparisons for 15 students). |
