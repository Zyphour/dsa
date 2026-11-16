# Student Guide — `linear_search.cpp`

This guide walks you through how [`linear_search.cpp`](linear_search.cpp) works and prepares you for questions an examiner might ask.

## How the Code Works

```cpp
int a[5], key;
cout << "Enter 5 elements: ";
for (int i = 0; i < 5; i++) cin >> a[i];
cout << "Enter value to search: "; cin >> key;
```
- `a[5]` is an integer array of size 5 (indices `0` to `4`).
- The first `for` loop reads 5 numbers from the keyboard and stores them in `a[0]` through `a[4]`.
- `key` stores the number the user wants to search for.

```cpp
for (int i = 0; i < 5; i++) {
    if (a[i] == key) { cout << "Found at position " << i + 1; return 0; }
}
cout << "Not Found";
return 0;
```
- The second `for` loop checks each slot from left to right.
- As soon as `a[i] == key` is true, it prints `i + 1` and hits `return 0;`, which **ends `main()` immediately** so `"Not Found"` does not get printed.
- Why `i + 1`? Arrays start at index `0`, so index `0` is position `1` for a normal user.
- If the loop finishes all 5 iterations without hitting `return 0;`, the element wasn't anywhere in `a`, so the next line prints `"Not Found"`.

## Dry Run

Input: `a = [10, 30, 20, 50, 40]`, `key = 20`

| `i` | `a[i]` | `a[i] == 20`? | Action |
|---|---|---|---|
| `0` | `10` | No | keep going |
| `1` | `30` | No | keep going |
| `2` | `20` | Yes | print `Found at position 3`, exit |

## Common Mistakes

- Forgetting `return 0;` (or a `found` flag) inside the `if` — then the program prints `"Not Found"` even after finding the number!
- Printing `i` instead of `i + 1` when asked for 1-based position.
- Using `i <= 5` instead of `i < 5` — accesses `a[5]` which is out of bounds.

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Does the array need to be sorted for Linear Search? | No, it works on both sorted and unsorted arrays. |
| What is the best-case and worst-case time complexity? | Best case is `O(1)` (found at index 0); worst case is `O(n)` (at the end or missing). |
| What happens if the same number appears twice? | It returns the position of the **first** occurrence because `return 0` exits right away. |
| When is Linear Search better than Binary Search? | When the array is unsorted or very small. |
