class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_left(self, current_node, value):
        current_node.left = Node(value)

    def add_right(self, current_node, value):
        current_node.right = Node(value)

    def print_tree(self, node, level=0):
        if node:
            print(" " * level * 2 + str(node.value))
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)

if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.add_left(tree.root, 5)
    tree.add_right(tree.root, 20)

    tree.add_left(tree.root.left, 3)
    tree.add_right(tree.root.left, 7)

    tree.print_tree(tree.root)
