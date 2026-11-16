# Student Guide — `binary_search.cpp`

This guide explains how [`binary_search.cpp`](binary_search.cpp) works and covers common questions for exams and viva.

## How the Code Works

```cpp
int arr[10], n, key, low, high, mid;
cout << "Enter the number of elements: "; cin >> n;
cout << "Enter the sorted elements: ";
for (int i = 0; i < n; i++) cin >> arr[i];
cout << "Enter the element to search: "; cin >> key;
```
- `arr[10]` can store up to 10 integers; `n` is how many numbers the user actually enters.
- Make sure the numbers you type are **already in ascending order** (e.g., `5 10 15 20 25`), otherwise Binary Search won't work properly.

```cpp
low = 0; high = n - 1;
while (low <= high) {
    mid = (low + high) / 2;
    if (arr[mid] == key) { cout << "Element found at position " << mid + 1; return 0; }
    else if (arr[mid] < key) low = mid + 1;
    else high = mid - 1;
}
cout << "Element not found.";
```
- `low` starts at index `0` and `high` starts at `n - 1`.
- The loop runs while `low <= high` (even when `low == high`, there is still 1 element left to check!).
- If `arr[mid] < key`, `key` is strictly greater than `arr[mid]`, so we skip `mid` and everything before it by setting `low = mid + 1`.
- Otherwise `arr[mid] > key`, so we skip `mid` and everything after it by setting `high = mid - 1`.
- If the loop finishes, `low` has crossed `high`, meaning the target isn't in the array.

## Dry Run

Input: `arr = [10, 20, 30, 40, 50]`, `n = 5`, `key = 40`

| Step | `low` | `high` | `mid` | `arr[mid]` | Comparison |
|---|---|---|---|---|---|
| 1 | `0` | `4` | `(0+4)/2 = 2` | `30` | `30 < 40` → `low = 3` |
| 2 | `3` | `4` | `(3+4)/2 = 3` | `40` | `40 == 40` → found at position `4`! |

## Common Mistakes

- Entering an **unsorted** array when testing — Binary Search assumes sorted order.
- Writing `while (low < high)` instead of `while (low <= high)` — misses the target when the search narrows down to 1 single element.
- Writing `low = mid` or `high = mid` instead of `mid + 1` / `mid - 1` — can cause an infinite loop!

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| What is the main requirement for Binary Search? | The data must be sorted beforehand. |
| Why is the time complexity `O(log n)`? | Every comparison cuts the remaining search range in half (`n → n/2 → n/4 ... → 1`). |
| Why do we use `low <= high` and not `low < high`? | Because when `low == high`, there is still one unexamined element at that index. |
| For 1,024 elements, how many comparisons does Binary Search take at most? | About `log2(1024) + 1 = 11` comparisons, compared to `1,024` in Linear Search. |
