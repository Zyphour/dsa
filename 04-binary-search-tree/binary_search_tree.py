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
