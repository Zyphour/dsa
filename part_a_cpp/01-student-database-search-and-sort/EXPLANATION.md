# Code explanation — `student_database.cpp`

Two globals hold the database:

```cpp
Student *arr = NULL;   // block of memory from malloc / realloc
int n = 0;             // number of records stored
```

## What each function does

| Function | Job |
|---|---|
| `addStudent()` | allocates with `malloc` for the first student and grows with `realloc` for each new student, then reads ID, name, CGPA |
| `display()` | prints `ID`, `Name`, `CGPA` separated by tabs |
| `linearSearch(key, comp)` | scans `0..n-1`, counts every comparison, returns index or `-1` |
| `binarySearch(key, comp)` | shrinks `low..high` using `mid = (low + high) / 2` |
| `sortById()` | bubble sort by `id` using `swap(arr[j], arr[j + 1])` |
| `sortByName()` | bubble sort by `name` using `strcmp` |
| `sortByCGPA(asc)` | selection sort by `cgpa` (`1` = ascending, `2` = descending) |

## Key lines

**Dynamic memory (`malloc` + `realloc`)**

```cpp
if (n == 0)
    arr = (Student*)malloc(sizeof(Student));
else
    arr = (Student*)realloc(arr, (n + 1) * sizeof(Student));
```

**Binary search**

```cpp
int mid = (low + high) / 2;
comp++;
if (arr[mid].id == key) return mid;
else if (arr[mid].id < key) low = mid + 1;
else high = mid - 1;
```

**Comparing Linear vs Binary search (Choice 7)**

```cpp
linearSearch(id, c1);
sortById();
binarySearch(id, c2);
```

Runs linear search before sorting (`c1`), sorts by ID, and runs binary search for
the same ID (`c2`), then `free(arr)` releases memory when exiting.

## Dry run — binary search for 104 in `[101, 102, 103, 104, 105]`

| Step | low | high | mid | value | Action | Comparisons |
|---|---|---|---|---|---|---|
| 1 | 0 | 4 | 2 | 103 | 103 < 104 → `low = 3` | 1 |
| 2 | 3 | 4 | 3 | 104 | equal → found at index 3 | 2 |

Linear search takes 4 comparisons here, and `n` in the worst case.

## Common mistakes

- Using `sizeof(Student*)` (pointer size) instead of `sizeof(Student)` (struct size).
- Running binary search without calling `sortById()` first.
- Swapping only one field instead of the entire `Student` struct (`swap(arr[j], arr[j + 1])`).
- Forgetting `free(arr)` before exit.

## Viva — short answers

| Question | Answer |
|---|---|
| `malloc` vs `realloc`? | malloc allocates a new block; realloc resizes an existing block and may move it. |
| Why is binary search O(log n)? | Half the remaining search range is discarded every comparison. |
| Is bubble sort stable? | Yes — it swaps only when the left key is strictly greater (`>`). |
| Selection sort advantage? | Makes at most `n − 1` swaps even in the worst case. |
| When is linear search better? | Unsorted or tiny data, or when searching only once. |
