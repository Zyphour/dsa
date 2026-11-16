class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        cur = root.right
        while cur.left:
            cur = cur.left
        root.key = cur.key
        root.right = delete(root.right, cur.key)
    return root


def search(root, key):
    while root:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))


def mirror(root):
    if root is None:
        return None
    n = Node(root.key)
    n.left = mirror(root.right)
    n.right = mirror(root.left)
    return n


def copy_tree(root):
    if root is None:
        return None
    n = Node(root.key)
    n.left = copy_tree(root.left)
    n.right = copy_tree(root.right)
    return n


def show_parents(root):
    if root:
        if root.left or root.right:
            l = root.left.key if root.left else "-"
            r = root.right.key if root.right else "-"
            print(root.key, "->", l, ",", r)
        show_parents(root.left)
        show_parents(root.right)


def show_leaves(root):
    if root:
        if root.left is None and root.right is None:
            print(root.key, end=" ")
        show_leaves(root.left)
        show_leaves(root.right)


def level_order(root):
    if root is None:
        return
    q = [root]
    while q:
        print([n.key for n in q])
        nxt = []
        for n in q:
            if n.left:
                nxt.append(n.left)
            if n.right:
                nxt.append(n.right)
        q = nxt


root = None
for x in [50, 30, 70, 20, 40, 60, 80, 40]:
    root = insert(root, x)

while True:
    print("\n1.Insert 2.Delete 3.Search 4.Traversals 5.Depth")
    print("6.Mirror 7.Copy 8.Parents 9.Leaves 10.LevelOrder 0.Exit")
    ch = input("Choice: ").strip()

    if ch == "1":
        root = insert(root, int(input("Value: ")))
    elif ch == "2":
        root = delete(root, int(input("Value: ")))
    elif ch == "3":
        print("Found" if search(root, int(input("Value: "))) else "Not Found")
    elif ch == "4":
        print("Inorder:", end=" "); inorder(root); print()
        print("Preorder:", end=" "); preorder(root); print()
        print("Postorder:", end=" "); postorder(root); print()
    elif ch == "5":
        print("Depth:", depth(root))
    elif ch == "6":
        m = mirror(root)
        print("Mirror Inorder:", end=" "); inorder(m); print()
    elif ch == "7":
        c = copy_tree(root)
        print("Copy Inorder:", end=" "); inorder(c); print()
    elif ch == "8":
        show_parents(root)
    elif ch == "9":
        print("Leaves:", end=" "); show_leaves(root); print()
    elif ch == "10":
        level_order(root)
    elif ch == "0":
        break
