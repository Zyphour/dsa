# Practical 4: Binary Search Tree (BST) — Complete Reference & Code Guide (`binary_search_tree.py`)

> **Aim:** Implement a Binary Search Tree in Python supporting insertion, search, deletion, and inorder traversal.
>
> **Language:** Python · **Program:** [`binary_search_tree.py`](binary_search_tree.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`binary_search_tree.py`](binary_search_tree.py) implements a **Binary Search Tree (BST)** using a `Node` class (`key`, `left`, `right`) and four recursive functions (`insert`, `search`, `delete`, `inorder`). When run, the script automatically executes a 4-step demonstration:
1. **Inserts** `[50, 30, 70, 20, 40, 60, 80]` into an initially empty BST (`root = None`).
2. **Searches** for key `40` and prints whether it was `"Found"` or `"Not Found"`.
3. **Deletes** key `30` (a node with **two children**, `20` and `40`, replacing `30` with its inorder successor `40`).
4. Runs **Inorder traversal** to print the remaining keys in ascending sorted order.

### Exact Program Output
```text
Search: Found
Inorder:
20 40 50 60 70 80 
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **BST** | **Full Form:** *Binary Search Tree* — a node-based binary tree where for every node `N`, **all keys in `N.left` are strictly less than `N.key`**, and **all keys in `N.right` are strictly greater than `N.key`**. |
| **Binary Tree** | A hierarchical non-linear data structure in which every node has **at most two children** (`left` child and `right` child). |
| **Root Node** | The topmost node of a tree (has no parent; `50` in our demo). |
| **Leaf Node (External Node)** | A node with **zero children** (`left is None and right is None`). |
| **Internal Node** | Any node that has **at least one child**. |
| **Height of a Tree (`h`)** | Number of edges (or levels) along the longest path from the root down to a leaf (`O(log n)` if balanced; `O(n)` if skewed). |
| **Skewed BST** | A degenerate BST where every node has only left children (left-skewed) or only right children (right-skewed, caused by inserting already-sorted data), behaving like a linked list of height `n`. |
| **Inorder Traversal** | Depth-first tree traversal visiting **`Left → Root → Right`**. On any BST, Inorder traversal **always outputs keys in ascending sorted order**. |
| **Preorder / Postorder** | **Preorder:** `Root → Left → Right`. **Postorder:** `Left → Right → Root`. |
| **Inorder Successor** | The **smallest key greater than `N.key`** — located at the **leftmost node of `N.right`** (`N.right`, then `.left` repeatedly). |
| **Inorder Predecessor** | The **largest key smaller than `N.key`** — located at the **rightmost node of `N.left`**. |
| **AVL Tree** | **Full Form:** *Adelson-Velsky and Landis Tree* — a self-balancing BST that keeps height `O(log n)` using rotations. |

---

## 3. Core Rules, Properties, Advantages & Uses

### The Three Deletion Cases in a BST (`delete(root, x)`)
1. **Case 1 — Node is a Leaf (0 children):** Unlink it by returning `None` to its parent.
2. **Case 2 — Node has 1 Child:** Bypass the node by returning its single non-`None` child (`root.left` or `root.right`) directly to its parent.
3. **Case 3 — Node has 2 Children:** Find its **Inorder Successor** `temp` (minimum node in `root.right`), copy `root.key = temp.key`, and recursively delete `temp.key` from `root.right`.

### Advantages & Disadvantages of BST
- **Advantages:**
  1. Fast **`O(log n)` average time** for `search`, `insert`, AND `delete` (unlike sorted arrays which need `O(n)` shifting on insert/delete, and unlike linked lists which need `O(n)` search).
  2. Maintains elements dynamically in sorted order (`inorder` prints sorted list in `O(n)`).
- **Disadvantages:**
  1. Without self-balancing, inserting sorted/reverse-sorted numbers creates a **skewed tree** where operations degrade to **O(n)**.
  2. Extra memory needed for two child references (`left`, `right`) per node.

### Uses / Applications of BST
1. Implementing **ordered Sets, Maps, and Dictionaries** (e.g., C++ `std::map` / `std::set` via Red-Black BSTs).
2. **Database indexing** and range queries (*"find all keys between X and Y"*).
3. **Symbol tables** in compilers and **auto-complete / priority lookup** tables.

---

## 4. Step-by-Step Algorithms

### `insert(root, x)`
1. If `root is None`, return `Node(x)`.
2. If `x < root.key`, set `root.left = insert(root.left, x)`.
3. Else if `x > root.key`, set `root.right = insert(root.right, x)`.
4. Return `root`.

### `search(root, x)`
1. If `root is None` or `root.key == x`, return `root`.
2. If `x < root.key`, return `search(root.left, x)`; else return `search(root.right, x)`.

### `delete(root, x)`
1. If `root is None`, return `None`.
2. If `x < root.key`, set `root.left = delete(root.left, x)`.
3. Else if `x > root.key`, set `root.right = delete(root.right, x)`.
4. Else (`x == root.key`):
   - If `root.left is None`, return `root.right` (handles 0 children & right-child-only).
   - If `root.right is None`, return `root.left` (handles left-child-only).
   - Find smallest node `temp` in `root.right` (`while temp.left: temp = temp.left`), set `root.key = temp.key`, and set `root.right = delete(root.right, temp.key)`.
5. Return `root`.

---

## 5. Line-by-Line Code Explanation

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
```

| Code Line / Block | Exact Role in the Program |
|---|---|
| `class Node: def __init__(self, x):` | Defines a tree node storing value `self.key = x` and initializing child pointers `left` and `right` to `None`. |
| `if root is None: return Node(x)` | Base case of `insert`: creates a new leaf node when an empty spot is reached. |
| `root.left = insert(root.left, x)` | Re-links returned subtree root onto `root.left` (ignores duplicate keys when `x == root.key`). |
| `if root is None or root.key == x: return root` | Base case of `search`: returns `None` if missing (falsy) or matching `Node` if found (truthy). |
| `if root.left is None: return root.right` | Handles both **leaf deletion** (returns `None`) and **1-right-child deletion**. |
| `if root.right is None: return root.left` | Handles **1-left-child deletion**. |
| `temp = root.right; while temp.left: temp = temp.left` | Locates the **inorder successor** (minimum key in right subtree) for 2-child deletion. |
| `root.key = temp.key; root.right = delete(root.right, temp.key)` | Replaces `root`'s key with successor's key and removes the duplicate successor node from `root.right`. |
| `inorder(root)` | Recursively traverses `left`, prints `root.key`, and traverses `right` (`Left → Root → Right`). |

---

## 6. Step-by-Step Dry Run

1. **Insert `[50, 30, 70, 20, 40, 60, 80]`:**
   ```text
           50
         /    \
       30      70
      /  \    /  \
     20  40  60  80
   ```
2. **`search(root, 40)`:** Checks `50` (`40 < 50` → left) → checks `30` (`40 > 30` → right) → hits `40` (`Found`).
3. **`delete(root, 30)`:** Node `30` has 2 children (`20` and `40`). Inorder successor in `30.right` is `40`. Copies `40` into `30`'s node and deletes leaf `40`:
   ```text
           50
         /    \
       40      70
      /       /  \
     20      60  80
   ```
4. **`inorder(root)`:** Visits `20 → 40 → 50 → 60 → 70 → 80`.

---

## 7. Time & Space Complexity Fact Sheet

Let `n` be the number of nodes and `h` be the tree height:

| Operation | Best / Average Time (Balanced, `h = log n`) | Worst-Case Time (Skewed, `h = n`) | Auxiliary Space (Recursion Stack) |
|---|---|---|---|
| **`insert(root, x)`** | **O(log n)** | **O(n)** | O(h) (`O(log n)` avg, `O(n)` worst) |
| **`search(root, x)`** | **O(log n)** | **O(n)** | O(h) |
| **`delete(root, x)`** | **O(log n)** | **O(n)** | O(h) |
| **`inorder(root)`** | **O(n)** | **O(n)** | O(h) |
| **Total Storage Space** | — | — | **O(n)** (stores `n` `Node` objects) |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Not reassigning `root = insert(root, x)` / `root = delete(root, x)`:** Discards updates whenever the root itself is created or deleted.
- **Mistake 2 — Forgetting `root.right = delete(root.right, temp.key)`:** Leaves a duplicate copy of the inorder successor in the right subtree.
- **Exam Fact:** Inserting already-sorted data (e.g., `10, 20, 30, 40`) produces a right-skewed chain of height `n`, causing worst-case **O(n)** search/insert/delete.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | What is the full form of BST and AVL? | **BST:** Binary Search Tree. **AVL:** Adelson-Velsky and Landis (self-balancing BST). |
| 2 | Define a Binary Search Tree (BST). | A binary tree in which for every node, all keys in its left subtree are smaller than the node's key and all keys in its right subtree are greater than the node's key. |
| 3 | Which traversal of a BST outputs elements in sorted ascending order? | **Inorder traversal (`Left → Root → Right`)**. |
| 4 | State the order of visits in Preorder, Inorder, and Postorder traversals. | **Preorder:** `Root → Left → Right`. **Inorder:** `Left → Root → Right`. **Postorder:** `Left → Right → Root`. |
| 5 | State the average-case and worst-case time complexities of `search`, `insert`, and `delete` in a BST. | Average case (balanced): **O(log n)**. Worst case (skewed tree): **O(n)**. |
| 6 | When does the worst case `O(n)` occur in a BST? | When elements are inserted in **already sorted or reverse-sorted order**, creating a skewed tree of height `n`. |
| 7 | State the time and space complexity of `inorder` traversal on `n` nodes. | Time complexity: **O(n)**. Space complexity: **O(h)** call stack (`O(n)` total tree storage). |
| 8 | What are the 3 cases of deleting a node in a BST? | (1) Deleting a **leaf node** (0 children), (2) deleting a node with **1 child**, and (3) deleting a node with **2 children** (replace with inorder successor or predecessor). |
| 9 | Define Inorder Successor of a node with two children. | The node with the **smallest key in its right subtree** (found at the leftmost node of `node.right`). |
| 10 | Where are the minimum and maximum elements located in a non-empty BST? | **Minimum:** the leftmost node of the tree. **Maximum:** the rightmost node of the tree. |
| 11 | Is a BST a linear or non-linear data structure? | **Non-linear** (hierarchical) data structure. |
| 12 | Give three applications/uses of Binary Search Trees. | (1) Ordered dictionaries/maps (`std::map`, `std::set`), (2) database indexing & range searches, and (3) compiler symbol tables. |
