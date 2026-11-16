# Code explanation — `student_database.cpp`

Menu-driven program. The three globals are the whole database:

```cpp
Student* students;   // block of memory from malloc / realloc
int count;           // records stored
int capacity;        // slots available
```

## What each function does

| Function | Job |
|---|---|
| `makeRoom()` | when full, `realloc` a block twice as big (2 → 4 → 8 …) and report it |
| `addStudent()` | read ID, name, CGPA into slot `count`, then `count++` |
| `displayStudents()` | formatted table using `setw` / `setprecision` |
| `linearSearch(id, comp)` | walk from index 0, count every comparison, return index or −1 |
| `binarySearch(arr, n, id, comp)` | shrink `low..high` using `low`/`high`/`mid` |
| `bubbleSort(byName)` | neighbour swaps; `true` = by name, `false` = by ID |
| `selectionSortCGPA(asc)` | pick the best CGPA, swap it to the front |
| `compareSearchPerformance()` | sorted copy + both searches on the same targets |

## Key lines

**Growing the array**

```cpp
Student* temp = (Student*)realloc(students, newCapacity * sizeof(Student));
if (temp == NULL) { ... }
students = temp;
```

The result goes into `temp` first. If `realloc` fails it returns `NULL`, and
writing that into `students` would lose the old block.

**Binary search**

```cpp
int mid = (low + high) / 2;
if (arr[mid].id == id)     return mid;
else if (arr[mid].id < id) low  = mid + 1;   // go right
else                       high = mid - 1;   // go left
```

**Sorting a whole record**

```cpp
Student temp = students[i];
students[i] = students[i + 1];
students[i + 1] = temp;
```

Swapping only the IDs would leave the names and CGPAs in the old order.

**Fair comparison**

```cpp
Student* sorted = (Student*)malloc(count * sizeof(Student));  // copy
// bubble sort the copy by ID
linearSearch(target, linComp);          // on the original (unsorted) array
binarySearch(sorted, count, target, binComp);
```

The copy protects the user's table (which may be sorted by name at that moment),
and `free(sorted)` releases it afterwards.

## Dry run — binary search for 104 in `[101, 102, 103, 104, 105]`

| Step | low | high | mid | value | Action | Comparisons |
|---|---|---|---|---|---|---|
| 1 | 0 | 4 | 2 | 103 | 103 < 104 → `low = 3` | 1 |
| 2 | 3 | 4 | 3 | 104 | equal → found at index 3 | 2 |

Linear search would take 4 comparisons here, and `n` in the worst case.

## Common mistakes

- Not checking the value returned by `realloc`.
- Using `sizeof(Student*)` (a pointer) instead of `sizeof(Student)` (the record).
- Running binary search after sorting by **name** — compile fine, wrong answers.
- Swapping only one field of the record.
- Forgetting `free(students)` before exit.

## Viva — short answers

| Question | Answer |
|---|---|
| `malloc` vs `realloc`? | malloc gives a new block; realloc resizes an existing one and may move it. |
| Why is binary search O(log n)? | The range halves every comparison. |
| Which sort is best on sorted data? | Bubble sort with the `swapped` flag (and insertion sort): O(n). |
| Is bubble sort stable? | Yes — it swaps only when the left key is strictly greater. |
| When is linear search better? | Unsorted or tiny data, or when you search only once. |
