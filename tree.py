class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_max_el(root):
    if root is None:
        return root
    
    current = root
    while current.right is not None:
        current = current.right
    return current.val

def find_min_el(root):
    if root is None:
        return root
    
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def find_sum(root):
    if root is None:
        return root
    
    current = root
    sum = current.val
    while current.left is not None:
        sum += current.left.val
        current = current.left
    current = root
    while current.right is not None:
        sum += current.right.val
        current = current.right
    return sum


root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root,15)
root = insert(root,1)

print(f"Max_element = {find_max_el(root)}")
print(f"Min_element = {find_min_el(root)}")
print(f"Suma = {find_sum(root)}")