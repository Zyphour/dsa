# Student Guide — `linear_binary_search.cpp`

This guide walks through [`linear_binary_search.cpp`](linear_binary_search.cpp), which lets the user pick between Linear Search and Binary Search using a `switch` menu.

## How the Code Works

```cpp
int arr[10], n, key, choice;
cout << "Enter the number of elements: "; cin >> n;
cout << "Enter the elements: ";
for (int i = 0; i < n; i++) cin >> arr[i];
cout << "\n----- MENU -----\n1. Linear Search\n2. Binary Search\nEnter your choice: "; cin >> choice;
cout << "Enter the element to search: "; cin >> key;
```
- Reads `n` elements (up to 10) into `arr`.
- Prints the menu, reads `choice`, and reads the search target `key`.

```cpp
switch (choice) {
    case 1:
        for (int i = 0; i < n; i++)
            if (arr[i] == key) { cout << "Element found at position " << i + 1; return 0; }
        cout << "Element not found."; break;
    case 2: {
        int low = 0, high = n - 1, mid;
        ...
        break;
    }
    default: cout << "Invalid Choice!";
}
```
- **`case 1`:** Runs Linear Search from `i = 0` to `n - 1`. Works whether `arr` is sorted or not.
- **`case 2`:** Notice the curly braces `{ ... }` around `case 2`! In C++, if you declare variables (`int low = 0, ...`) inside a `switch` case without braces, jumping to `default:` crosses variable initialization and fails to compile. Wrapping `case 2` in `{ ... }` gives those variables their own block scope.
- **`default`:** Runs if the user enters anything other than `1` or `2`.

## Dry Run

- Input: `n = 5`, `arr = [4, 8, 12, 16, 20]`, `choice = 2`, `key = 16`
- `low = 0, high = 4` → `mid = 2` (`12 < 16` → `low = 3`)
- `low = 3, high = 4` → `mid = 3` (`16 == 16`) → prints `Element found at position 4`.

## Common Mistakes

- Picking **Binary Search (2)** after typing unsorted numbers — Binary Search will give the wrong result on unsorted data!
- Declaring variables inside a `case` in C++ without `{ }` braces (causes a compiler error).
- Forgetting `break;` at the end of a `case` (causes execution to fall into the next case).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Compare Linear Search and Binary Search. | Linear works on any array in `O(n)`; Binary needs a sorted array and runs in `O(log n)`. |
| Why does `case 2` need `{ }` braces in C++? | Because it declares and initializes local variables (`low`, `high`, `mid`); without a block, jumping to `default:` causes a compile error. |
| What does `default:` do in a `switch`? | Catches any `choice` value that doesn't match `1` or `2`. |
