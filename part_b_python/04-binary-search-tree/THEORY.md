# Practical 4 — Binary Search Tree

**Aim:** Implement a BST with insert (duplicates handled), delete, search,
traversals, depth, mirror image, copy, parents with children, leaf nodes and
level-wise display.

**Language:** Python · **Program:** [`binary_search_tree.py`](binary_search_tree.py)

---

## Concepts

A **tree** has a root, nodes, and leaves (nodes with no children). A **binary
tree** gives every node at most two children.

**BST rule:** for every node, everything in the **left** subtree is smaller and
everything in the **right** subtree is bigger.

```
            50
          /    \
        30      70
       /  \    /  \
      20  40  60  80
```

Because of the rule a search only walks down one branch, so the cost is the
height of the tree: `O(log n)` when balanced, `O(n)` in the worst case (inserting
sorted data makes a chain).

## Operations

| Operation | Idea |
|---|---|
| Insert | compare at each node, go left if smaller, right if bigger, attach at the empty spot |
| Search | same walk; stop when found or when the pointer becomes `None` |
| Delete | three cases — leaf, one child, two children |
| Traversals | inorder (sorted), preorder, postorder, level order (BFS) |
| Depth | `1 + max(depth(left), depth(right))`, `depth(None) = 0` |
| Mirror | swap left and right at every node |
| Copy | create a new node for every node (deep copy) |
| Leaves | nodes where both children are `None` |

**Duplicates.** The program sends a duplicate to the **right** subtree, so no
record is lost and the BST rule still holds. Valid alternatives: reject the
duplicate, or keep a `count` inside the node.

**Delete, three cases**

1. **Leaf** → remove it (parent gets `None`).
2. **One child** → the child takes the node's place.
3. **Two children** → copy the smallest key of the right subtree (inorder
   successor) into the node, then delete that key from the right subtree.

## Complexity

| Operation | Average | Worst | Space |
|---|---|---|---|
| Insert / Search / Delete | O(log n) | O(n) | O(n) |
| Traversals, depth, mirror, copy, leaves | O(n) | O(n) | O(h) recursion |

`h` = height of the tree.

## Exam points

- Inorder of a BST is always sorted — that is the standard proof of the rule.
- Preorder matches prefix notation, postorder matches postfix notation.
- Postorder is the right traversal for freeing a tree (children before parent).
- A mirrored BST prints its inorder in descending order.
- Deep copy = new nodes; shallow copy would share the same nodes.
