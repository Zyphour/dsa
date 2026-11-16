"""
EXPERIMENT 4 : Binary Search Tree (BST)
---------------------------------------
Part B - Python

A Binary Search Tree is a binary tree with one rule:
    everything in the LEFT subtree  is SMALLER than the node
    everything in the RIGHT subtree is BIGGER  than the node

            50
          /    \
        30      70
       /  \    /  \
      20  40  60  80

Because of that rule a search only walks down ONE branch, so it is fast
O(log n) when the tree is balanced and O(n) in the worst case.

Operations implemented
    a) insert   (a duplicate value is pushed to the right, so it is not lost)
    b) delete   (3 cases: leaf, one child, two children)
    c) search
    d) traversals (inorder, preorder, postorder)
    e) depth of the tree
    f) mirror image
    g) copy of the tree
    h) all parent nodes with their children
    i) leaf nodes
    j) level wise display (BFS)

Run: python3 binary_search_tree.py
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# ----------------------------------------------------------------------
# a) INSERT
# ----------------------------------------------------------------------
def insert(root, key):
    if root is None:                 # empty place found -> put the node here
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        # DUPLICATE: we do not crash and we do not drop the value.
        # We simply store it in the right subtree (a fixed, simple rule).
        print(f"   note: {key} already exists, duplicate kept in the right subtree")
        root.right = insert(root.right, key)

    return root


# ----------------------------------------------------------------------
# b) DELETE
# ----------------------------------------------------------------------
def find_min(node):
    """smallest key in a subtree = left-most node"""
    while node.left is not None:
        node = node.left
    return node


def delete(root, key):
    if root is None:
        return None                        # key not found

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # key found -> 3 cases
        if root.left is None and root.right is None:      # case 1: leaf
            return None
        if root.left is None:                             # case 2: only right child
            return root.right
        if root.right is None:                            # case 2: only left child
            return root.left

        # case 3: two children -> replace with smallest of right subtree,
        # then delete that smallest value from the right subtree
        successor = find_min(root.right)
        root.key = successor.key
        root.right = delete(root.right, successor.key)

    return root


# ----------------------------------------------------------------------
# c) SEARCH
# ----------------------------------------------------------------------
def search(root, key):
    steps = 0
    while root is not None:
        steps += 1
        if key == root.key:
            return True, steps
        elif key < root.key:
            root = root.left             # go left, forget the right side
        else:
            root = root.right            # go right, forget the left side
    return False, steps


# ----------------------------------------------------------------------
# d) TRAVERSALS
# ----------------------------------------------------------------------
def inorder(root, out):
    if root is not None:
        inorder(root.left, out)
        out.append(root.key)
        inorder(root.right, out)
    return out


def preorder(root, out):
    if root is not None:
        out.append(root.key)
        preorder(root.left, out)
        preorder(root.right, out)
    return out


def postorder(root, out):
    if root is not None:
        postorder(root.left, out)
        postorder(root.right, out)
        out.append(root.key)
    return out


# ----------------------------------------------------------------------
# e) DEPTH (height) OF THE TREE
# ----------------------------------------------------------------------
def depth(root):
    if root is None:
        return 0                    # an empty tree has depth 0
    return 1 + max(depth(root.left), depth(root.right))


# ----------------------------------------------------------------------
# f) MIRROR IMAGE  (left and right of every node are swapped)
# ----------------------------------------------------------------------
def mirror(root):
    if root is None:
        return None
    new_node = Node(root.key)
    new_node.left = mirror(root.right)      # right becomes left
    new_node.right = mirror(root.left)      # left becomes right
    return new_node


# ----------------------------------------------------------------------
# g) COPY OF THE TREE  (deep copy: brand new nodes)
# ----------------------------------------------------------------------
def copy_tree(root):
    if root is None:
        return None
    new_node = Node(root.key)
    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)
    return new_node


# ----------------------------------------------------------------------
# h) PARENT NODES WITH THEIR CHILDREN
# ----------------------------------------------------------------------
def show_parents(root, out):
    if root is not None:
        if root.left is not None or root.right is not None:
            left = root.left.key if root.left else "-"
            right = root.right.key if root.right else "-"
            out.append((root.key, left, right))
        show_parents(root.left, out)
        show_parents(root.right, out)
    return out


# ----------------------------------------------------------------------
# i) LEAF NODES (nodes with no children)
# ----------------------------------------------------------------------
def show_leaves(root, out):
    if root is not None:
        if root.left is None and root.right is None:
            out.append(root.key)
        show_leaves(root.left, out)
        show_leaves(root.right, out)
    return out


# ----------------------------------------------------------------------
# j) LEVEL WISE DISPLAY  (Breadth First Search, uses a queue)
# ----------------------------------------------------------------------
def level_order(root):
    if root is None:
        return []
    levels = []
    queue = [root]                     # simple list used as a queue
    while queue:
        level = []
        next_queue = []
        for node in queue:
            level.append(node.key)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        levels.append(level)
        queue = next_queue
    return levels


# ----------------------------------------------------------------------
# pretty sideways tree print (root on the left)
# ----------------------------------------------------------------------
def print_tree(root, space=0):
    if root is None:
        return
    space += 6
    print_tree(root.right, space)
    print(" " * (space - 6) + str(root.key))
    print_tree(root.left, space)


# ----------------------------------------------------------------------
# MENU
# ----------------------------------------------------------------------
def show_all(root):
    if root is None:
        print("Tree is empty.")
        return
    print("\n--- Tree (sideways, right side is on top) ---")
    print_tree(root)
    print("Inorder   (sorted) :", inorder(root, []))
    print("Preorder           :", preorder(root, []))
    print("Postorder          :", postorder(root, []))
    print("Level wise         :", level_order(root))
    print("Depth              :", depth(root), "levels")


def main():
    root = None

    # a small sample tree so the menu is not empty
    for key in [50, 30, 70, 20, 40, 60, 80, 40]:
        root = insert(root, key)
    print("Sample tree loaded (note the duplicate 40).")

    while True:
        print("\n============ BINARY SEARCH TREE ============")
        print("1.  Insert")
        print("2.  Delete")
        print("3.  Search")
        print("4.  Display tree + traversals")
        print("5.  Depth of tree")
        print("6.  Mirror image")
        print("7.  Copy the tree")
        print("8.  Parents with their children")
        print("9.  Leaf nodes")
        print("10. Level wise display")
        print("0.  Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            key = int(input("Key to insert: "))
            root = insert(root, key)
            print("Inserted.")

        elif choice == "2":
            key = int(input("Key to delete: "))
            root = delete(root, key)
            print("Deleted (if it existed).")

        elif choice == "3":
            key = int(input("Key to search: "))
            found, steps = search(root, key)
            if found:
                print(f"FOUND in {steps} step(s).")
            else:
                print(f"NOT FOUND ({steps} step(s) walked).")

        elif choice == "4":
            show_all(root)

        elif choice == "5":
            if root is None:
                print("Tree is empty, depth = 0")
            else:
                print(f"Depth = {depth(root)} levels "
                      f"(height in edges = {depth(root) - 1})")

        elif choice == "6":
            if root is None:
                print("Tree is empty.")
            else:
                mirrored = mirror(root)
                print("Original inorder:", inorder(root, []))
                print("Mirror   inorder:", inorder(mirrored, []), "(now descending)")
                print("Mirror tree:")
                print_tree(mirrored)

        elif choice == "7":
            duplicate = copy_tree(root)
            print("Copy created. Inorder of copy:", inorder(duplicate, []))
            print("Both trees have separate nodes, so changing one does not")
            print("change the other (that is what a deep copy means).")

        elif choice == "8":
            rows = show_parents(root, [])
            if not rows:
                print("No parent nodes (tree empty or only one node).")
            else:
                print(f"{'PARENT':>8} {'LEFT':>8} {'RIGHT':>8}")
                for p, l, r in rows:
                    print(f"{p:>8} {l:>8} {r:>8}")

        elif choice == "9":
            leaves = show_leaves(root, [])
            print("Leaf nodes:", leaves)

        elif choice == "10":
            if root is None:
                print("Tree is empty.")
            else:
                for i, level in enumerate(level_order(root), start=1):
                    print(f"Level {i}: {level}")

        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
