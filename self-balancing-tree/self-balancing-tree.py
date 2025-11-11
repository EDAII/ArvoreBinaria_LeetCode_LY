class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.ht = 0

def height(node):
    if node is None:
        return -1
    return node.ht

def update_height(node):
    if node is not None:
        node.ht = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(root, new_val):
    if root is None:
        return Node(new_val)
    
    if new_val < root.val:
        root.left = insert(root.left, new_val)
    else:
        root.right = insert(root.right, new_val)
    
    update_height(root)
    
    bf = balance_factor(root)
    
    if bf > 1 and new_val < root.left.val:
        return rotate_right(root)
    
    if bf < -1 and new_val > root.right.val:
        return rotate_left(root)
    
    if bf > 1 and new_val > root.left.val:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    
    if bf < -1 and new_val < root.right.val:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    
    return root

def inorder(node, result): #esquerda, raiz, direita
    if node is None:
        return
    inorder(node.left, result)
    result.append(f"{node.val}(BF={balance_factor(node)})")
    inorder(node.right, result)

def preorder(node, result): #raiz, esquerda, direita
    if node is None:
        return
    result.append(f"{node.val}(BF={balance_factor(node)})")
    preorder(node.left, result)
    preorder(node.right, result)

n = int(input())
values = list(map(int, input().split()))
new_val = int(input())

root = None
for val in values:
    root = insert(root, val)

root = insert(root, new_val)

result = []
inorder(root, result)
print(" ".join(result))

result = []
preorder(root, result)
print(" ".join(result))