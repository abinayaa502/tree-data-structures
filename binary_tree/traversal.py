class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Inorder Traversal 
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

# Preorder Traversal 
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

# Postorder Traversal 
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

# Level Order Traversal 
from collections import deque

def level_order(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder: ")
    inorder(root)
    print("\nPreorder: ")
    preorder(root)
    print("\nPostorder: ")
    postorder(root)
    print("\nLevel Order: ")
    level_order(root)
