# Practical 4 — Binary Search Tree (BST)

**Aim:** Implement a Binary Search Tree in Python supporting insertion, search,
deletion, and inorder traversal.

**Language:** Python · **Program:** [`binary_search_tree.py`](binary_search_tree.py)

---

## Concepts

- **BST property** – for every node `x`, all keys in `x.left` are smaller than
  `x.key` and all keys in `x.right` are greater than `x.key`.
- **Inorder traversal (`Left → Node → Right`)** – visits every BST key in sorted
  ascending order.

| Operation | Average (balanced) | Worst (skewed) |
|---|---|---|
| `insert` | O(log n) | O(n) |
| `search` | O(log n) | O(n) |
| `delete` | O(log n) | O(n) |
| `inorder` | O(n) | O(n) |

## Algorithm

### `insert(root, x)` & `search(root, x)`
1. If `root is None`: return `Node(x)` (for insert) or `None` (for search).
2. If `x < root.key`, recurse into `root.left`; if `x > root.key`, recurse into
   `root.right`.

### `delete(root, x)`
1. Walk left/right until `root.key == x`.
2. Handle the 3 deletion cases:
   - **0 children (leaf)** or **1 child:** return `root.right` (if `left` is
     `None`) or `root.left` (if `right` is `None`).
   - **2 children:** find the smallest node `temp` in `root.right` (inorder
     successor), copy `root.key = temp.key`, and delete `temp.key` from
     `root.right`.

## Exam points

- Deleting a node with two children replaces it with its **inorder successor**
  (leftmost node in right subtree) or **inorder predecessor** (rightmost in left).
- Inserting already-sorted numbers produces a skewed chain of height `n` (time
  degrades to `O(n)`).
- Space complexity is `O(n)` for storing `n` nodes.
