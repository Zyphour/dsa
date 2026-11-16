# Code explanation — `binary_search_tree.py`

Node structure:

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

Loads `[50, 30, 70, 20, 40, 60, 80, 40]` initially (including duplicate `40`).

## What each function does

| Function | Job |
|---|---|
| `insert(root, key)` | `<` goes left, `>=` goes right (duplicates stored on the right) |
| `delete(root, key)` | handles 0/1 child with `if root.left is None` / `if root.right is None`, and 2 children via inorder successor `cur` |
| `search(root, key)` | iterative walk returning `True` or `False` |
| `inorder` / `preorder` / `postorder` | recursive traversals printing keys |
| `depth(root)` | `0` if `None`, else `1 + max(depth(left), depth(right))` |
| `mirror(root)` | creates a mirrored tree with `left` and `right` swapped |
| `copy_tree(root)` | deep copy creating new `Node` instances |
| `show_parents(root)` | prints `parent -> left , right` for every non-leaf node |
| `show_leaves(root)` | prints keys where both `left` and `right` are `None` |
| `level_order(root)` | BFS queue `q`, printing one list of keys per level |

## Key parts

**Insert (including duplicates):**

```python
if root is None:
    return Node(key)
if key < root.key:
    root.left = insert(root.left, key)
else:
    root.right = insert(root.right, key)
return root
```

**Delete (all 3 cases in 9 lines):**

```python
if root.left is None:
    return root.right     # covers leaf (None) and right-only child
if root.right is None:
    return root.left      # left-only child
cur = root.right          # two children: leftmost node of right subtree
while cur.left:
    cur = cur.left
root.key = cur.key
root.right = delete(root.right, cur.key)
```

## Dry run — sample tree

| Query | Result |
|---|---|
| inorder | `20 30 40 40 50 60 70 80` |
| preorder | `50 30 20 40 40 70 60 80` |
| depth | `4` |
| leaves | `20 40 60 80` |
| parents | `50 -> 30 , 70`, `30 -> 20 , 40`, `40 -> - , 40`, `70 -> 60 , 80` |
| delete 50 | inorder successor `60` replaces `50`, then `60` is deleted from right subtree |

## Common mistakes

- Calling `insert(root.left, key)` without assigning back to `root.left`.
- Returning `1` instead of `0` for `depth(None)`.
- Writing `c = root` (shallow alias) instead of creating new `Node` objects in `copy_tree`.

## Viva — short answers

| Question | Answer |
|---|---|
| Why is inorder sorted? | Left (smaller) is visited before root, then right (larger). |
| Worst case of BST? | O(n) when keys are inserted in sorted order (skewed tree). |
| How to delete a 2-child node? | Copy inorder successor's key into the node, then delete the successor. |
| Which traversal deletes/frees a tree? | Postorder (children before parent). |
