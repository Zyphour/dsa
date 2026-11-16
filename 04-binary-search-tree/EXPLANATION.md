# Student Guide — `binary_search_tree.py`

This guide explains how [`binary_search_tree.py`](binary_search_tree.py) works and prepares you for viva questions.

## How the Code Works

- **`Node` class:** Stores `self.key` and initializes `self.left = self.right = None`.
- **`insert(root, x)`:**
  - Notice `root = insert(root, x)` is always assigned back! Why? When the tree is empty (`root is None`), `insert` creates and returns the new `Node(x)` so the caller's `root` (or `root.left` / `root.right`) gets updated.
  - Duplicate keys (`x == root.key`) don't match `<` or `>`, so they are ignored.
- **`search(root, x)`:**
  - Returns the `Node` if found (truthy in Python) or `None` if missing (falsy).
- **`delete(root, x)`:**
  - When `x == root.key` (we found the node to remove):
    - `if root.left is None: return root.right` handles **both** "no children" (returns `None`) and "only right child" (returns right child).
    - `if root.right is None: return root.left` handles "only left child".
    - For **two children**: `temp = root.right; while temp.left: temp = temp.left` finds the smallest value larger than `root.key` (the inorder successor), copies `temp.key` up, and deletes `temp.key` from the right subtree.
- **`inorder(root)`:** Visits `left`, prints `key`, visits `right` — always prints BST keys in sorted order.

## Dry Run

1. Inserts `[50, 30, 70, 20, 40, 60, 80]` → `50` at root, `30` left (`20`, `40`), `70` right (`60`, `80`).
2. `search(root, 40)` → `50 → 30 → 40` → prints `Search: Found`.
3. `delete(root, 30)` → `30` has two children (`20` and `40`), so inorder successor `40` replaces `30` and the old `40` leaf is removed.
4. `inorder(root)` prints `20 40 50 60 70 80`.

## Common Mistakes

- Calling `insert(root, x)` or `delete(root, x)` without saving the returned value back into `root = ...` (changes to the root node would be lost!).
- Forgetting to delete `temp.key` from `root.right` after copying `root.key = temp.key` (leaves a duplicate node in the tree).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Which traversal of a BST gives sorted output? | Inorder traversal (`Left → Root → Right`). |
| What are the three cases in BST deletion? | Leaf (0 children), 1 child, and 2 children (replace with inorder successor or predecessor). |
| What is the worst-case time complexity of BST search, and when does it happen? | `O(n)` when elements are inserted in sorted/reverse-sorted order, creating a skewed tree. |
| What is an inorder successor? | The smallest node in a node's right subtree (the leftmost node of `root.right`). |
