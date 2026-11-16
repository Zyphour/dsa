# Code explanation — `binary_search_tree.py`

A node holds a key and two links:

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

The program loads a sample tree at start — `50, 30, 70, 20, 40, 60, 80, 40` —
which contains a duplicate `40` on purpose.

## What each function does

| Function | Job |
|---|---|
| `insert(root, key)` | recursive insert; duplicate → right subtree with a printed note |
| `find_min(node)` | left-most node = smallest key in a subtree |
| `delete(root, key)` | the three cases; case 3 reuses `find_min` |
| `search(root, key)` | loop down the tree, return `(found, steps)` |
| `inorder` / `preorder` / `postorder` | collect keys in the three orders |
| `depth(root)` | levels in the tree |
| `mirror(root)` | returns a **new** tree with left/right swapped |
| `copy_tree(root)` | returns a new, identical tree |
| `show_parents(root, out)` | rows of `(parent, left child, right child)` |
| `show_leaves(root, out)` | keys of nodes with no children |
| `level_order(root)` | BFS with a queue, one list per level |
| `print_tree(root, space)` | sideways drawing (rotated 90°), right side on top |

## Key parts

**Insert** — the recursion does the walking, and the assignment fixes the link:

```python
if key < root.key:      root.left  = insert(root.left, key)
elif key > root.key:    root.right = insert(root.right, key)
else:                   root.right = insert(root.right, key)   # duplicate
```

**Delete, case 3:**

```python
successor = find_min(root.right)      # smallest key bigger than the node
root.key = successor.key
root.right = delete(root.right, successor.key)
```

**Depth:**

```python
if root is None: return 0
return 1 + max(depth(root.left), depth(root.right))
```

**Level order** keeps two lists — the current level and the next one — which
avoids managing indices in a single queue.

## Dry run — sample tree

```
50
├── 30
│    ├── 20
│    └── 40
│         └── 40   (duplicate)
└── 70
     ├── 60
     └── 80
```

| Query | Result |
|---|---|
| inorder | `20 30 40 40 50 60 70 80` (sorted) |
| preorder | `50 30 20 40 40 70 60 80` |
| depth | 4 levels (height 3 edges) |
| leaves | `20, 40, 60, 80` |
| parents | `(50,30,70) (30,20,40) (40,-,40) (70,60,80)` |
| search 999 | not found, walks 50 → 70 → 80 then stops |
| delete 50 | successor 60 replaces it, then 60 is removed from the right subtree |

## Common mistakes

- Writing `insert(root.left, key)` without assigning it back — the new node is lost.
- Removing a two-child node directly, which breaks the ordering rule.
- `depth(None) = 1`, which over-counts the levels by one.
- Mirroring only the root's children instead of every node.
- Building a copy by writing `new_root = root`, which is only a second name for
  the same tree (shallow copy).

## Viva — short answers

| Question | Answer |
|---|---|
| Why is inorder sorted? | Smaller keys are visited first, then the node, then bigger ones. |
| Worst case of a BST? | O(n) — a chain formed by inserting sorted data. |
| Delete a node with two children? | Replace with the inorder successor, then delete the successor. |
| Which traversal frees a tree? | Postorder. |
| Mirror image? | Swap left and right at every node, recursively. |
