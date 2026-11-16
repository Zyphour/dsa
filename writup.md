# Data Structures and Algorithms Collection

This repository contains simplified implementations of common data structures and algorithms. The programs have been simplified, comments reduced, and code quality adjusted to focus on core logic and explanations.

## Programs Section

### Part A: C++ Programs (part_a_cpp/)

#### 1. Student Database Management
**File:** `part_a_cpp/01-student-database-search-and-sort/student_database.cpp`
**Name:** Student Database Management
**Explanation:** Stores student records (roll, name, cgpa) and sorts them by roll number using bubble sort. Simplified implementation.
**Simplified Code:**
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

#### 2. Binary Search
**File:** `part_a_cpp/01-student-database-search-and-sort/Binary Search.cpp`
**Name:** Binary Search C++ Program
**Explanation:** Finds an element in a sorted array by repeatedly dividing the search interval in half.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int arr[10], n, key, low, high, mid;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the sorted elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "Enter the element to search: "; cin >> key;
    low = 0; high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (arr[mid] == key) { cout << "Element found at position " << mid + 1; return 0; }
        else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    cout << "Element not found.";
    return 0;
}
```

#### 3. Bubble Sort
**File:** `part_a_cpp/01-student-database-search-and-sort/Bubble Sort.cpp`
**Name:** Bubble Sort C++ Program
**Explanation:** Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int a[100], n, temp;
    cout << "Enter size: "; cin >> n;
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (a[j] > a[j + 1]) { temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp; }
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    return 0;
}
```

#### 4. Insertion Sort
**File:** `part_a_cpp/01-student-database-search-and-sort/Insertion Sort.cpp`
**Name:** Insertion Sort C++ Program
**Explanation:** Builds the final sorted array one item at a time by inserting each element into its correct position.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int a[5], key, j;
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) cin >> a[i];
    for (int i = 1; i < 5; i++) {
        key = a[i]; j = i - 1;
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
        a[j + 1] = key;
    }
    cout << "Sorted array: ";
    for (int i = 0; i < 5; i++) cout << a[i] << " ";
    return 0;
}
```

#### 5. Linear Search
**File:** `part_a_cpp/01-student-database-search-and-sort/Linear Search.cpp`
**Name:** Linear Search C++ Program
**Explanation:** Sequentially checks each element of the list for the target value until a match is found or the whole list has been searched.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int a[5], key;
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) cin >> a[i];
    cout << "Enter value to search: "; cin >> key;
    for (int i = 0; i < 5; i++) {
        if (a[i] == key) { cout << "Found at position " << i + 1; return 0; }
    }
    cout << "Not Found";
    return 0;
}
```

#### 6. Selection Sort
**File:** `part_a_cpp/01-student-database-search-and-sort/Selection Sort.cpp`
**Name:** Selection Sort C++ Program
**Explanation:** Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int arr[100], n, temp;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++) cin >> arr[i];
    for(int i = 0; i < n - 1; i++) {
        int min = i;
        for(int j = i + 1; j < n; j++)
            if(arr[j] < arr[min]) min = j;
        temp = arr[i]; arr[i] = arr[min]; arr[min] = temp;
    }
    cout << "Sorted array: ";
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    return 0;
}
```

#### 7. Linear-Binary Search Menu
**File:** `part_a_cpp/01-student-database-search-and-sort/Linear-Binary Search.cpp`
**Name:** Linear and Binary Search Menu Program
**Explanation:** Provides a menu-driven interface to choose between linear search and binary search on an array.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int arr[10], n, key, choice;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "\n----- MENU -----\n1. Linear Search\n2. Binary Search\nEnter your choice: "; cin >> choice;
    cout << "Enter the element to search: "; cin >> key;
    switch (choice) {
        case 1:
            for (int i = 0; i < n; i++)
                if (arr[i] == key) { cout << "Element found at position " << i + 1; return 0; }
            cout << "Element not found."; break;
        case 2:
            int low = 0, high = n - 1, mid;
            while (low <= high) {
                mid = (low + high) / 2;
                if (arr[mid] == key) { cout << "Element found at position " << mid + 1; return 0; }
                else if (arr[mid] < key) low = mid + 1;
                else high = mid - 1;
            }
            cout << "Element not found."; break;
        default: cout << "Invalid Choice!";
    }
    return 0;
}
```

#### 8. Circular Queue
**File:** `part_a_cpp/03-circular-queue-array/circular_queue.cpp`
**Name:** Circular Queue Implementation
**Explanation:** A queue data structure where the last position is connected back to the first position to make a circle.
**Simplified Code:**
```cpp
#include <iostream>
using namespace std;
int q[5], f = -1, r = -1;
void enqueue(int x) {
    if ((r + 1) % 5 == f) cout << "Full";
    else { if (f == -1) f = 0; r = (r + 1) % 5; q[r] = x; }
}
void dequeue() {
    if (f == -1) cout << "Empty";
    else { cout << "Deleted: " << q[f]; if (f == r) f = r = -1; else f = (f + 1) % 5; }
}
void display() {
    if (f == -1) cout << "Empty";
    else {
        for (int i = f; ; i = (i + 1) % 5) { cout << q[i] << " "; if (i == r) break; }
    }
}
int main() {
    int ch, x;
    do {
        cout << "\n1.Enqueue 2.Dequeue 3.Display 4.Exit\n"; cin >> ch;
        switch (ch) {
            case 1: cin >> x; enqueue(x); break;
            case 2: dequeue(); break;
            case 3: display(); break;
        }
    } while (ch != 4);
    return 0;
}
```

### Part B: Python Programs (part_b_python/)

#### 9. Binary Search Tree
**File:** `part_b_python/04-binary-search-tree/binary_search_tree.py`
**Name:** Binary Search Tree Operations
**Explanation:** Implements a binary search tree with insertion, search, deletion, and inorder traversal.
**Simplified Code:**
```python
class Node:
    def __init__(self, x):
        self.key = x
        self.left = self.right = None

def insert(root, x):
    if root is None: return Node(x)
    if x < root.key: root.left = insert(root.left, x)
    elif x > root.key: root.right = insert(root.right, x)
    return root

def search(root, x):
    if root is None or root.key == x: return root
    if x < root.key: return search(root.left, x)
    return search(root.right, x)

def delete(root, x):
    if root is None: return root
    if x < root.key: root.left = delete(root.left, x)
    elif x > root.key: root.right = delete(root.right, x)
    else:
        if root.left is None: return root.right
        if root.right is None: return root.left
        temp = root.right
        while temp.left: temp = temp.left
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None
for x in [50, 30, 70, 20, 40, 60, 80]: root = insert(root, x)
print("Search:", "Found" if search(root, 40) else "Not Found")
root = delete(root, 30)
print("Inorder:")
inorder(root)
```

#### 10. Heap Sort
**File:** `part_b_python/06-heap-sort/heap_sort.py`
**Name:** Heap Sort Algorithm
**Explanation:** Sorts an array by first building a max heap and then repeatedly extracting the maximum element.
**Simplified Code:**
```python
def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]: largest = left
    if right < n and a[right] > a[largest]: largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1): heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

print(heap_sort([4, 10, 3, 5, 1]))
```

#### 11. Merge Sort
**File:** `part_b_python/07-merge-sort-orders/merge_sort_orders.py`
**Name:** Merge Sort Algorithm
**Explanation:** Divides the array into halves, sorts them recursively, and merges the sorted halves.
**Simplified Code:**
```python
def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort([8, 3, 5, 1, 9, 2]))
```

#### 12. Fractional Knapsack
**File:** `part_b_python/08-fractional-knapsack/fractional_knapsack.py`
**Name:** Fractional Knapsack Problem
**Explanation:** Calculates the maximum profit by selecting fractions of items based on profit/weight ratio.
**Simplified Code:**
```python
def knapsack(items, cap):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    profit = 0
    for p, w in items:
        take = min(w, cap)
        profit += take * p/w
        cap -= take
        if cap == 0: break
    return profit

items = [(60,10), (100,20), (120,30)]
print(knapsack(items, 50))
```

#### 13. Naive String Matching
**File:** `part_b_python/09-naive-string-matching/naive_string_matching.py`
**Name:** Naive String Matching Algorithm
**Explanation:** Searches for occurrences of a pattern within a text by checking every possible starting position.
**Simplified Code:**
```python
def naive_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == pattern[j]: j += 1
        if j == m: positions.append(i)
    return positions

print(naive_match("ABABABCABAB", "ABAB"))
```

## Summary
This collection provides simplified implementations of fundamental data structures and algorithms. Each program focuses on the core logic with minimal comments and straightforward code structure, making them suitable for quick reference and understanding. Programs are organized according to the repository structure:
- **Part A (C++)**: Located in `part_a_cpp/` directory
- **Part B (Python)**: Located in `part_b_python/` directory

## Usage
- C++ programs can be compiled and run with `g++ filename.cpp -o program && ./program`
- Python programs can be run directly with `python3 filename.py`
- Each program includes basic input/output handling for demonstration purposes
- Each program directory also contains EXPLANATION.md and THEORY.md files with additional details
