# Student Guide — `student_database.cpp`

This guide helps you understand [`student_database.cpp`](student_database.cpp) line by line and prepares you for viva questions.

## How the Code Works

```cpp
struct Student { int roll; string name; float cgpa; };
```
- Creates a blueprint called `Student` that bundles three variables together. Each `s[i]` in `Student s[15]` has its own `s[i].roll`, `s[i].name`, and `s[i].cgpa`.

```cpp
for(int i=0; i<15; i++) cin >> s[i].roll >> s[i].name >> s[i].cgpa;
```
- Reads 15 students from standard input. Since `cin >> s[i].name` stops at whitespace, type single-word names (like `Aman`, `Riya`).

```cpp
for(int i=0; i<14; i++)
    for(int j=0; j<14-i; j++)
        if(s[j].roll > s[j+1].roll) { temp = s[j]; s[j] = s[j+1]; s[j+1] = temp; }
```
- Standard Bubble Sort for `n = 15` (so `n - 1 = 14`).
- Notice we compare `.roll` (`s[j].roll > s[j+1].roll`), **but** inside `{ ... }` we copy `s[j]` as a whole struct into `temp`! In C++, assigning one struct to another copies all fields (`roll`, `name`, `cgpa`) automatically.

## Dry Run (shown with 3 records)

Input:
```text
103 Neha 8.9
101 Aman 9.2
102 Riya 8.5
```
- Pass 1: compares `103` & `101` → swaps `(101 Aman)` and `(103 Neha)`; compares `103` & `102` → swaps `(102 Riya)` and `(103 Neha)`.
- Pass 2: compares `101` & `102` → no swap.

Output:
```text
101 Aman 9.2
102 Riya 8.5
103 Neha 8.9
```

## Common Mistakes

- Swapping only `s[j].roll` and `s[j+1].roll` instead of the whole `Student` struct — that mixes up roll numbers with the wrong names and CGPAs!
- Typing spaces inside a student's name when using `cin >> s[i].name` (a space breaks `cin` and shifts the remaining inputs).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Why use a `struct` instead of 3 separate arrays? | A `struct` keeps related fields (`roll`, `name`, `cgpa`) grouped in one object, so swapping `s[j]` and `s[j+1]` moves all fields together cleanly. |
| How would you sort by CGPA instead of roll number? | Change the `if` condition to `s[j].cgpa < s[j+1].cgpa` (for highest CGPA first). |
| What is the time complexity of this sort? | `O(n²)` because of the nested Bubble Sort loops. |
